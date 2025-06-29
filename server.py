from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up!"}

connected_players = []

class Player(BaseModel):
    player_name: str


@app.post("/connect")
def connect_player(player: Player):
    connected_players.append(player.player_name)
    print(connected_players)
    return {"message": f"Player {player.player_name} connected successfully"}

rooms = []

class Room(BaseModel):
    room_name: str
    host_player: str
    max_player :int = 6
    players: list[str] = []
    status: str = "waiting"

@app.post("/create_room")
def create_room(room: Room):
    for existing_room in rooms:
        if existing_room.room_name == room.room_name:
            return {"error": "Room name already exists."}
        
    room.players = [room.host_player]
    rooms.append(room)
    print(rooms)
    return {"message": f"Room '{room.room_name}' created by {room.host_player}."}


@app.post("/join_room")
def join_room(player_name: str, room_name: str):
    for room in rooms:
        if room.room_name == room_name:
            if room.status != "waiting":
                raise HTTPException(status_code=403, detail="Cannot join; game already in progress.")

            if player_name in room.players:
                return {"error": "f{player_name} is already in the room."}
            
            if len(room.players) >= room.max_player:
                return {"error": "Room is full."}
            
            room.players.append(player_name)
            print(f"{player_name} joined room '{room_name}'. Current players: {room.players}")
            return {"message": f"{player_name} joined room '{room_name}' successfully."}
    
    raise HTTPException(status_code=404, detail="Room not found.")


@app.post("/leave_room")
def leave_room(player_name:str, room_name: str):
    for room in rooms:
        if room.room_name == room_name:
            if player_name in room.players:
                room.players.remove(player_name)

                if len(room.players) == 0:
                    rooms.remove(room)
                    return {"message": f"'{room_name}' room was closed because there are no players left."}
                
                if player_name == room.host_player:
                    room.host_player = room.players[0]
                    return {"message": f"Host player left so '{room.host_player} is the new host"}
                
                return {"message": f"{player_name} left room '{room_name}' successfully."} 
            
            else:
                raise HTTPException(status_code=404, detail="Player not found in this room.")

    raise HTTPException(status_code=404, detail="Room not found.")


