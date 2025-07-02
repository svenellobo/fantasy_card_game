from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, UTC

app = FastAPI()




class Player(BaseModel):
    player_name: str
    joined_room: Optional[str] = None
    is_host: bool = False


class Room(BaseModel):
    room_name: str
    host_player: str
    max_player: int = 6
    players: list[str] = Field(default_factory=list)
    status: str = "waiting"


class RoomCreateRequest(BaseModel):
    room_name: str
    host_player_name: str

class LeaveRoomRequest(BaseModel):
    room_name: str
    player_name: str

class Message(BaseModel):
    author: str
    text: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))


connected_players: list[Player] = []
rooms: list[Room] = []
message_board: list["Message"] = []


@app.get("/")
def read_root():
    return {"message": "Server is up!"}


@app.post("/connect")
def connect_player(player: Player):
    if any(p.player_name == player.player_name for p in connected_players):
        raise HTTPException(status_code=400, detail="Player with this name already connected.")
    connected_players.append(player)
    return {"message": f"Player {player.player_name} connected successfully"}


@app.post("/create_room")
def create_room(req: RoomCreateRequest):
    for existing_room in rooms:
        if existing_room.room_name == req.room_name:
            return {"error": "Room name already exists."}

    stored_player = next((p for p in connected_players if p.player_name == req.host_player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Host player not connected.")

    stored_player.joined_room = req.room_name
    stored_player.is_host = True

    created_room = Room(
        room_name=req.room_name,
        host_player=stored_player.player_name,        
        players=[req.host_player_name]
    )
    
    rooms.append(created_room)

    return {"message": f"Room '{created_room.room_name}' created by {created_room.host_player}."}

@app.post("/join_room")
def join_room(player: Player, room_name: str):
    stored_player = next((p for p in connected_players if p.player_name == player.player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")

    for room in rooms:
        if room.room_name == room_name:
            if room.status != "waiting":
                raise HTTPException(status_code=403, detail="Cannot join; game already in progress.")

            if any(p_name == stored_player.player_name for p_name in room.players):
                return {"error": f"{stored_player.player_name} is already in the room."}

            if len(room.players) >= room.max_player:
                return {"error": "Room is full."}

            room.players.append(stored_player.player_name)
            stored_player.joined_room = room_name

            return {"message": f"{stored_player.player_name} joined room '{room_name}' successfully."}

    raise HTTPException(status_code=404, detail="Room not found.")


@app.post("/leave_room")
def leave_room(req: LeaveRoomRequest):
    stored_player = next((p for p in connected_players if p.player_name == req.player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")

    for room in rooms:
        if room.room_name == req.room_name:
            if any(p_name == stored_player.player_name for p_name in room.players):
                room.players = [p_name for p_name in room.players if p_name != stored_player.player_name]
                stored_player.joined_room = None

                if len(room.players) == 0:
                    rooms.remove(room)
                    return {"message": f"'{req.room_name}' room was closed because there are no players left."}

                if stored_player.player_name == room.host_player:
                    stored_player.is_host = False

                    new_host_name = room.players[0]
                    room.host_player = new_host_name
                    new_host_player = next((p for p in connected_players if p.player_name == new_host_name), None)

                    if new_host_player:
                        new_host_player.is_host = True

                    return {"message": f"Host player left. '{room.host_player}' is the new host."}

                return {"message": f"{stored_player.player_name} left room '{req.room_name}' successfully."}
            else:
                raise HTTPException(status_code=404, detail="Player not found in this room.")

    raise HTTPException(status_code=404, detail="Room not found.")

@app.get("/list_rooms")
def list_rooms():
     return [
        {
            "room_name": room.room_name,
            "host_player": room.host_player,
            "num_players": len(room.players),
            "max_player": room.max_player,
            "status": room.status
        }
        for room in rooms
    ]

@app.post("/start_game")
def start_game(room_name: str):
    for room in rooms:
        if room.room_name == room_name:
            if room.status != "waiting":
                raise HTTPException(status_code=400, detail="Game already started or room not in waiting state.")
            room.status = "playing"
            return {"message": f"Game in room '{room_name}' started successfully."}
    raise HTTPException(status_code=404, detail="Room not found.")

@app.post("/end_game")
def end_game(room_name: str):
    for room in rooms:
        if room.room_name == room_name:
            if room.status != "playing":
                raise HTTPException(status_code=400, detail="Game is not in progress.")
            room.status = "finished"
            return {"message": f"Game in room '{room_name}' ended successfully."}
        
    raise HTTPException(status_code=404, detail="Room not found.")

@app.post("/disconnect")
def disconnect(player_name: str):
    stored_player = next((p for p in connected_players if p.player_name == player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not found.")

    if stored_player.joined_room:
        for room in rooms:
            if room.room_name == stored_player.joined_room:
                room.players = [p_name for p_name in room.players if p_name != stored_player.player_name]

                if len(room.players) == 0:
                    rooms.remove(room)
                    return {"message": f"Player '{player_name}' disconnected successfully. Room '{room.room_name}' was closed because it had no players."}

                elif stored_player.player_name == room.host_player:
                    stored_player.is_host = False
                    new_host_name = room.players[0]
                    room.host_player = new_host_name
                    room.host_player.is_host = True

                    new_host_player = next((p for p in connected_players if p.player_name == new_host_name), None)
                    if new_host_player:
                        new_host_player.is_host = True
                break

    connected_players.remove(stored_player)
    return {"message": f"Player '{player_name}' disconnected successfully."}


@app.post("/post_message")
def post_message(msg: Message):
    if not msg.author.strip():
        raise HTTPException(status_code=400, detail="Author cannot be empty.")
    if not msg.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty.") 
    
    msg.timestamp = datetime.now(UTC)
    message_board.append(msg)

    return {"message": "Message posted successfully."}


@app.get("/get_messages")
def get_messages(limit: int = 50):    
    sorted_msgs = sorted(message_board, key=lambda x: x.timestamp, reverse=True)
    return sorted_msgs[:limit]


