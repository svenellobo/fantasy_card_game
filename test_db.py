import unittest
import sqlite3
import os
import database

class TestDBFunctions(unittest.TestCase):
    def setUp(self):               
        self.test_db = "test_game.db"
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS players")
            cursor.execute("DROP TABLE IF EXISTS rooms")
        
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT,
                    joined_room TEXT,
                    is_host BOOLEAN DEFAULT 0
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_name TEXT,
                    host_player TEXT,
                    status TEXT DEFAULT 'waiting'
                )
            """)
            conn.commit()

    def tearDown(self):        
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_player(self):        
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO players (player_name) VALUES (?)", ("Sven",))
            conn.commit()
            cursor.execute("SELECT * FROM players WHERE player_name = ?", ("Sven",))
            player = cursor.fetchone()
            self.assertIsNotNone(player)
            self.assertEqual(player[1], "Sven")

    def test_create_room(self):
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rooms (room_name, host_player) VALUES (?, ?)", ("Room1", "Sven"))
            conn.commit()
            cursor.execute("SELECT * FROM rooms WHERE room_name = ?", ("Room1",))
            room = cursor.fetchone()
            self.assertIsNotNone(room)
            self.assertEqual(room[1], "Room1")
            self.assertEqual(room[2], "Sven")
            self.assertNotEqual(room[2], "John")

    def test_update_room_status(self):
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rooms (room_name, host_player) VALUES (?, ?)", ("Room2", "John"))
            conn.commit()
            cursor.execute("UPDATE rooms SET status = ? WHERE room_name = ?", ("playing", "Room2"))
            conn.commit()
            cursor.execute("SELECT status FROM rooms WHERE room_name = ?", ("Room2",))
            status = cursor.fetchone()[0]
            self.assertEqual(status, "playing")

if __name__ == "__main__":
    unittest.main()