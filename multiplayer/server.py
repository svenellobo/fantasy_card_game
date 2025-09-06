from fastapi import FastAPI, HTTPException
import socketio
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, UTC
import database as db
from multiplayer.server_multiplayer_game import ServerMultiplayerGame


app = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app.mount("/ws", socketio.ASGIApp(sio))

@sio.event
async def socket_join_room(sid, data):
    room_name = data["room_name"]
    sio.enter_room(sid, room_name)

db.create_tables()

games = {}


class Player(BaseModel):
    player_name: str
    joined_room: Optional[str] = None
    is_host: bool = False


class Room(BaseModel):
    room_name: str
    host_player: str   
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




@app.get("/")
def read_root():
    return {"message": "Server is up!"}


@app.post("/connect")
def connect_player(player: Player):    
    if db.get_player(player.player_name):
        raise HTTPException(status_code=400, detail="Player with this name already connected.")
    db.add_player(player.player_name)    
    return {"message": f"Player {player.player_name} connected successfully"}


@app.post("/create_room")
def create_room(req: RoomCreateRequest):    
    if db.get_room(req.room_name):
        return {"error": "Room name already exists."}
    
    stored_player = db.get_player(req.host_player_name)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Host player not connected.")

    previous_room = stored_player["joined_room"]
    db.create_room(req.room_name, req.host_player_name)

    if previous_room and previous_room != req.room_name:
        prev_players = db.list_players_in_room(previous_room)
        if len(prev_players) == 0:
            db.delete_room(previous_room)       

    return {"message": f"Room '{req.room_name}' created by {req.host_player_name}."}

@app.post("/join_room")
def join_room(player_name: str, room_name: str):
    stored_player = db.get_player(player_name)    
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")
    
    previous_room = stored_player["joined_room"]
    fetched_room = db.get_room(room_name)
    if fetched_room:
        if fetched_room["status"] != "waiting":
            raise HTTPException(status_code=403, detail="Cannot join; game already in progress.")
        
        if stored_player["joined_room"] == room_name:
            raise HTTPException(status_code=400, detail=f"{stored_player["player_name"]} is already in the room.")
                
        list_players = db.list_players_in_room(room_name)
        if len(list_players) >= 6:            
            return {"error": "Room is full."}

        db.update_player_joined_room(room_name, stored_player["player_name"])

        if previous_room and previous_room != room_name:
            prev_players = db.list_players_in_room(previous_room)
            if len(prev_players) == 0:
                db.delete_room(previous_room)

        return {"message": f"{stored_player['player_name']} joined room '{room_name}' successfully."}
    
    else:
        raise HTTPException(status_code=404, detail="Room not found.")


@app.post("/leave_room")
def leave_room(req: LeaveRoomRequest):    
    stored_player = db.get_player(req.player_name)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")
    
    fetched_room = db.get_room(req.room_name)    
    if fetched_room:
        if not fetched_room:
            raise HTTPException(status_code=404, detail="Room not found.")
        
        if stored_player["joined_room"] != fetched_room["room_name"]:
            raise HTTPException(status_code=404, detail="Player not found in this room.")
        
        db.update_player_joined_room(None, stored_player["player_name"])
        
        game = games.get(fetched_room["room_name"])
        if game:
            game.players.pop(stored_player["player_name"], None)
            if len(game.players) <= 1:
                result = game.end_game()
                games.pop(fetched_room["room_name"], None)
                db.delete_room(fetched_room["room_name"])
                return {"message": f"Player '{stored_player['player_name']}' disconnected. Game ended because it had less than 2 players.","result": result} 

        if game.current_player_name == stored_player["player_name"]:
            game.end_turn(stored_player["player_name"])

        list_players = db.list_players_in_room(fetched_room["room_name"])
        if not list_players:
            db.delete_room(fetched_room["room_name"])
            return {"message": f"{stored_player['player_name']} left and room '{fetched_room['room_name']}' was deleted (empty)."}

        if stored_player["player_name"] == fetched_room["host_player"]:
            new_host = list_players[0]["player_name"]
            db.update_player_is_host(stored_player["player_name"], 0)
            db.update_player_is_host(new_host, 1)
            db.update_room_host(fetched_room["room_name"], new_host)
            return {"message": f"Host player left. '{new_host}' is the new host."}

    return {"message": f"{stored_player['player_name']} left room '{fetched_room['room_name']}' successfully."}

@app.get("/list_rooms")
def list_rooms():
    list_of_rooms = db.list_rooms()
    return [
        {
            "room_name": room["room_name"],
            "host_player": room["host_player"],
            "num_players": len(db.list_players_in_room(room["room_name"])),
            "status": room["status"]
        }
        for room in list_of_rooms
    ]



@app.post("/end_game")
def end_game(room_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")
    result = game.end_game()
    games.pop(room_name, None)
    return result

@app.post("/disconnect")
def disconnect(player_name: str):
    stored_player = db.get_player(player_name)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not found.")

    room_name = stored_player["joined_room"]
    if room_name:
        fetched_room = db.get_room(room_name)
        db.update_player_joined_room(None, player_name)

        game = games.get(room_name)
        if game:
            game.players.pop(player_name, None)
            if len(game.players) <= 1:
                result = game.end_game()
                games.pop(room_name, None)
                db.delete_room(room_name)                
                db.remove_player(player_name)
                return {"message": f"Player '{player_name}' disconnected. Game ended because it had less than 2 players.", "result": result}
            if game.current_player_name == player_name:
                game.end_turn(player_name)

        
        list_players = db.list_players_in_room(room_name)
        if fetched_room:
            if fetched_room["host_player"] == player_name:
                if list_players:
                    new_host = list_players[0]["player_name"]
                    db.update_player_is_host(new_host, 1)
                    db.update_room_host(room_name, new_host)
                else:
                    db.delete_room(room_name)
            else:
                if not list_players:
                    db.delete_room(room_name)
    
    db.remove_player(player_name)
    return {"message": f"Player '{player_name}' disconnected successfully."}
            
    


@app.post("/start_game")
async def start_game(room_name: str):
    fetched_room = db.get_room(room_name)
    if not fetched_room:
        raise HTTPException(status_code=404, detail="Room not found.")

    if fetched_room["status"] != "waiting":
        raise HTTPException(status_code=400, detail="Game already started or room not in waiting state.")

    db.update_room_status("playing", fetched_room["room_name"])
    players = db.list_players_in_room(room_name)
    player_names = [p["player_name"] for p in players]
    game = ServerMultiplayerGame(player_names)
    games[room_name] = game

    await sio.emit("game_started", {"room_name": room_name}, room=room_name)

    return {"message": f"Game in room '{room_name}' started successfully.", "players": player_names}
    

@app.post("/draw_card")
def draw_card(room_name: str, player_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Game not running in this room.")
    try:
        return game.draw_card(player_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/discard_card")
def discard_card(room_name: str, player_name: str, card_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")
    try:
        result = game.discard_card(player_name, card_name)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.post("/take_from_discard")
def take_from_discard(room_name: str, player_name: str, card_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")
    try:
        return game.take_from_discard(player_name, card_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))




@app.post("/end_turn")
def end_turn(room_name: str, player_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")

    try:
        result = game.end_turn(player_name)
        if result.get("status") == "game_over":
            fetched_room = db.get_room(room_name)
            if fetched_room and fetched_room["status"] == "playing":
                db.update_room_status("finished", fetched_room["room_name"])
            games.pop(room_name, None)
            #TODO nisam siguran za games.pop ovdje
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/list_players_in_room")
def list_players_in_room(room_name: str):
    players = db.list_players_in_room(room_name)
    return players



@app.get("/get_room")
def get_room(room_name: str):
    fetched_room = db.get_room(room_name)
    if not fetched_room:
        raise HTTPException(status_code=404, detail="Room not found.")    
    return fetched_room


@app.get("/get_player")
def get_player(player_name: str):
    fetched_player = db.get_player(player_name)
    if not fetched_player:
        raise HTTPException(status_code=404, detail="Player not found.")    
    return fetched_player

