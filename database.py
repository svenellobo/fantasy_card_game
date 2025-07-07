import sqlite3


def create_tables():
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT,
                joined_room TEXT,
                is_host BOOLEAN DEFAULT 0         
            )        
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_name TEXT,
                host_player TEXT,
                status TEXT DEFAULT 'waiting'    
            )
            """
        )
        conn.commit()


def add_player(player_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO players (player_name) VALUES (?)",
            (player_name,)
        )
        conn.commit()

def update_player_joined_room(room_name, player_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE players SET joined_room = ? WHERE player_name = ?",
            (room_name, player_name)
        )
        conn.commit()


def update_player_is_host(player_name, is_host):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE players SET is_host = ? WHERE player_name = ?", (is_host, player_name)
        )
        conn.commit()

def remove_player(player_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM players WHERE player_name = ?",
            (player_name,)
        )
        conn.commit()

def create_room(room_name, host_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO rooms (room_name, host_player) VALUES (?, ?)",
            (room_name, host_name)
        )
        cursor.execute(
            "UPDATE players SET is_host = 1 WHERE player_name = ?",
            (host_name,)
        )
        conn.commit()

def delete_room(room_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM rooms WHERE room_name = ?",
            (room_name,)
        )
        conn.commit()

def update_room_status(status, room_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE rooms SET status = ? WHERE room_name = ?",
            (status, room_name)
        )
        conn.commit()

def update_room_host(room_name, host_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE rooms SET host_player = ? WHERE room_name = ?",
            (host_name, room_name)
        )
        conn.commit()

def get_room(room_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM rooms WHERE room_name = ?",
            (room_name,)
        )
        return cursor.fetchone()

def get_player(player_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM players WHERE player_name = ?",
            (player_name,)
        )
        return cursor.fetchone()

def list_rooms():
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM rooms")           
        
        return cursor.fetchall()
    
def list_players_in_room(room_name):
    with sqlite3.connect("game.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM players WHERE joined_room = ?",
            (room_name,)
        )
        return cursor.fetchall()