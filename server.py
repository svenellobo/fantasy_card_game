from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, UTC
import database as db
from multiplayer_game import MultiplayerGame

app = FastAPI()

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

    db.create_room(req.room_name, req.host_player_name)
    db.update_player_joined_room(req.room_name, req.host_player_name)    

    return {"message": f"Room '{req.room_name}' created by {req.host_player_name}."}

@app.post("/join_room")
def join_room(player_name: str, room_name: str):
    stored_player = db.get_player(player_name)    
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")
    
    fetched_room = db.get_room(room_name)
    if fetched_room:
        if fetched_room[3] != "waiting":
            raise HTTPException(status_code=403, detail="Cannot join; game already in progress.")
        
        if stored_player[2] == room_name:
            raise HTTPException(status_code=400, detail=f"{stored_player[1]} is already in the room.")
                
        list_players = db.list_players_in_room(room_name)
        if len(list_players) >= 6:            
            return {"error": "Room is full."}

        db.update_player_joined_room(room_name, stored_player[1])

        return {"message": f"{stored_player[1]} joined room '{room_name}' successfully."}
    
    else:
        raise HTTPException(status_code=404, detail="Room not found.")


@app.post("/leave_room")
def leave_room(req: LeaveRoomRequest):    
    stored_player = db.get_player(req.player_name)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not connected.")
    
    fetched_room = db.get_room(req.room_name)
    if fetched_room:        
        if stored_player[2] == fetched_room[1]:
            db.update_player_joined_room(None, stored_player[1])

            list_players = db.list_players_in_room(fetched_room[1])
            if len(list_players) <= 1:                
                if len(list_players) == 1:
                    db.update_player_joined_room(None, list_players[0][1])
                db.delete_room(fetched_room[1])
                return {"message": f"'{req.room_name}' room was closed because there are no players left."}          

            
            if stored_player[1] == fetched_room[2]:
                db.update_player_is_host(stored_player[1], 0)
                db.update_player_is_host(list_players[0][1], 1)            
                db.update_room_host(fetched_room[1], list_players[0][1])

                return {"message": f"Host player left. '{fetched_room[2]}' is the new host."}

            return {"message": f"{stored_player[1]} left room '{fetched_room[1]}' successfully."}
        else:
            raise HTTPException(status_code=404, detail="Player not found in this room.")

    raise HTTPException(status_code=404, detail="Room not found.")

@app.get("/list_rooms")
def list_rooms():
    list_of_rooms = db.list_rooms()
    return [
        {
            "room_name": room[1],
            "host_player": room[2],
            "num_players": len(db.list_players_in_room(room[1])),
            "status": room[3]
        }
        for room in list_of_rooms
    ]


@app.post("/end_game")
def end_game(room_name: str):
    fetched_room = db.get_room(room_name)
    if fetched_room:
        if fetched_room[3] != "playing":
            raise HTTPException(status_code=400, detail="Game is not in progress.")
        db.update_room_status("finished", fetched_room[1])
        return {"message": f"Game in room '{room_name}' ended successfully."}
        
    raise HTTPException(status_code=404, detail="Room not found.")

@app.post("/disconnect")
def disconnect(player_name: str):
    stored_player = db.get_player(player_name)
    if not stored_player:
        raise HTTPException(status_code=404, detail="Player not found.")

    if stored_player[2]:
        fetched_room = db.get_room(stored_player[2])                
        db.update_player_joined_room(None, stored_player[1])

        list_players = db.list_players_in_room(fetched_room[1])
        if len(list_players) <= 1:                
            if len(list_players) == 1:
                db.update_player_joined_room(None, list_players[0][1])
            db.delete_room(fetched_room[1])
            return {"message": f"Player '{stored_player[1]}' disconnected successfully. Room '{fetched_room[1]}' was closed because it had no players."}
        
        if fetched_room[2] == stored_player[1]:
            db.update_player_is_host(list_players[0][1], 1)            
            db.update_room_host(fetched_room[1], list_players[0][1])
            
    db.remove_player(stored_player[1])
    return {"message": f"Player '{stored_player[1]}' disconnected successfully."}


@app.post("/start_game")
def start_game(room_name: str):
    fetched_room = db.get_room(room_name)
    if not fetched_room:
        raise HTTPException(status_code=404, detail="Room not found.")

    if fetched_room[3] != "waiting":
        raise HTTPException(status_code=400, detail="Game already started or room not in waiting state.")

    db.update_room_status("playing", fetched_room[1])
    players = db.list_players_in_room(room_name)
    player_names = [p[1] for p in players]
    game = MultiplayerGame(player_names)
    games[room_name] = game

    return {"message": f"Game in room '{room_name}' started successfully.", "players": player_names}
    

@app.post("/draw_card")
def draw_card(room_name: str, player_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Game not running in this room.")
    card = game.deck.draw_card()
    player = game.players[player_name]    
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in game.")
    player.cards_in_hand.append(card)
    return {"card_name": card.name}

@app.post("/discard_card")
def discard_card(room_name: str, player_name: str, card_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")
    player = game.players[player_name]
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in game.")

    disc_card = next((card for card in player.cards_in_hand if card.name == card_name), None)

    if not disc_card:
        raise HTTPException(status_code=404, detail="Card not found in hand.")
    player.cards_in_hand.remove(disc_card)
    game.discard_area.discard_area_cards.append(disc_card)
    return {"message": f"{disc_card.name} discarded successfully"}


@app.post("/end_turn")
def end_turn(room_name: str, player_name: str):
    game = games.get(room_name)
    if not game:
        raise HTTPException(status_code=404, detail="Room not found.")
    
    if game.current_player_name != player_name:
        raise HTTPException(status_code=403, detail="It is not your turn.")
    game.end_turn()
    return {"message": "Turn ended", "next_player": game.get_current_player()}



"""@app.post("/post_message")
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
    return sorted_msgs[:limit]"""


