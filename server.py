from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up!"}


class Player(BaseModel):
    player_name: str
    joined_room: Optional[str] = None
    is_host: bool = False

connected_players: list[Player] = []

@app.post("/connect")
def connect_player(player: Player):
    if any(p.player_name == player.player_name for p in connected_players):
        raise HTTPException(status_code=400, detail="Player with this name already connected.")
    connected_players.append(player)
    return {"message": f"Player {player.player_name} connected successfully"}

class Room(BaseModel):
    room_name: str
    host_player: Player
    max_player: int = 6
    players: list[Player] = Field(default_factory=list)
    status: str = "waiting"

rooms: list[Room] = []

@app.post("/create_room")
def create_room(room: Room):
    for existing_room in rooms:
        if existing_room.room_name == room.room_name:
            return {"error": "Room name already exists."}

    stored_player = next((p for p in connected_players if p.player_name == room.host_player.player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Host player not connected.")

    stored_player.joined_room = room.room_name
    stored_player.is_host = True
    room.players = [stored_player]
    room.host_player = stored_player
    rooms.append(room)

    return {"message": f"Room '{room.room_name}' created by {room.host_player.player_name}."}

@app.post("/join_room")
def join_room(player: Player, room_name: str):
    stored_player = next((p for p in connected_players if p.player_name == player.player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")

    for room in rooms:
        if room.room_name == room_name:
            if room.status != "waiting":
                raise HTTPException(status_code=403, detail="Cannot join; game already in progress.")

            if any(p.player_name == stored_player.player_name for p in room.players):
                return {"error": f"{stored_player.player_name} is already in the room."}

            if len(room.players) >= room.max_player:
                return {"error": "Room is full."}

            room.players.append(stored_player)
            stored_player.joined_room = room_name

            return {"message": f"{stored_player.player_name} joined room '{room_name}' successfully."}

    raise HTTPException(status_code=404, detail="Room not found.")


@app.post("/leave_room")
def leave_room(player: Player, room_name: str):
    stored_player = next((p for p in connected_players if p.player_name == player.player_name), None)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")

    for room in rooms:
        if room.room_name == room_name:
            if any(p.player_name == stored_player.player_name for p in room.players):
                room.players = [p for p in room.players if p.player_name != stored_player.player_name]
                stored_player.joined_room = None

                if len(room.players) == 0:
                    rooms.remove(room)
                    return {"message": f"'{room_name}' room was closed because there are no players left."}

                if stored_player.player_name == room.host_player.player_name:
                    stored_player.is_host = False
                    room.host_player = room.players[0]
                    room.host_player.is_host = True

                    return {"message": f"Host player left. '{room.host_player.player_name}' is the new host."}

                return {"message": f"{stored_player.player_name} left room '{room_name}' successfully."}
            else:
                raise HTTPException(status_code=404, detail="Player not found in this room.")

    raise HTTPException(status_code=404, detail="Room not found.")

@app.get("/list_rooms")
def list_rooms():
    return [room.model_dump() for room in rooms]

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
    player = next((p for p in connected_players if p.player_name == player_name), None)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found.")

    if player.joined_room:
        for room in rooms:
            if room.room_name == player.joined_room:
                room.players = [p for p in room.players if p.player_name != player.player_name]
                if len(room.players) == 0:
                    rooms.remove(room)
                elif player.player_name == room.host_player.player_name:
                    player.is_host = False
                    room.host_player = room.players[0]
                    room.host_player.is_host = True
                break

    connected_players.remove(player)
    return {"message": f"Player '{player_name}' disconnected successfully."}




                    
                    


        
    


        
            
    


    
            