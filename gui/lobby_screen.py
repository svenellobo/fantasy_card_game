import customtkinter as ctk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from gui.multiplayer_game_screen import MultiplayerGameScreen
from multiplayer.local_multiplayer_game import LocalMultiplayerGame
from multiplayer.server import RoomCreateRequest, LeaveRoomRequest, create_room
import requests
from constants import SERVER_URL



class LobbyScreen(ctk.CTkFrame):
    def __init__(self, parent, player_name):
        super().__init__(parent)
        self.parent = parent        
        self.selected_room_name = None
        self.player_name = player_name
        self.room_buttons = []
        

        self.parent.protocol("WM_DELETE_WINDOW", self.on_app_close)
        
        self.grid(row=0, column=0, sticky="nsew")
        self.configure(fg_color="#4E342E")
        self.init_screen()


    def init_screen(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0, minsize=100)
        self.grid_rowconfigure(2, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0, minsize=200) 
        self.grid_columnconfigure(2, weight=1)


        self.main_area = ctk.CTkFrame(self, fg_color="#6D4C41")
        self.main_area.grid(row=1, column=1, pady=5, padx=5)

        self.lobby_area = ctk.CTkFrame(self.main_area, fg_color="#800000")
        self.lobby_area.grid(row=0, column=0, pady=5, padx=5) 

        self.lobby_area_lbl = ctk.CTkLabel(self.lobby_area, fg_color="green", font=("Verdana Arial", 14, "bold"), text="List of available rooms:")
        self.lobby_area_lbl.grid(row=0, column=0, pady=5, padx=5)        

        self.room_list_frame = ctk.CTkScrollableFrame(self.lobby_area, width=300, height=400)
        self.room_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")

        self.btns_frame = ctk.CTkFrame(self.main_area)
        self.btns_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.create_btn = ctk.CTkButton(self.btns_frame, text="Create Room", font=("Verdana Arial", 14, "bold"), height=60, command=self.create_room_button_press, fg_color="green")
        self.create_btn.grid(row=0, column=0, padx=10, pady=10)

        self.join_btn = ctk.CTkButton(self.btns_frame, text="Join Room", font=("Verdana Arial", 14, "bold"), height=60, fg_color="#800000", state="disabled")
        self.join_btn.grid(row=2, column=0, padx=10, pady=10)

        self.refresh_btn = ctk.CTkButton(self.btns_frame, text="Refresh", font=("Verdana Arial", 14, "bold"), height=60, fg_color="green")
        self.refresh_btn.grid(row=1, column=0, padx=10, pady=10)        

        self.start_game_btn = ctk.CTkButton(self.btns_frame, text="Start Game", font=("Verdana Arial", 14, "bold"), height=60, fg_color="#800000", state="disabled")
        self.start_game_btn.grid(row=3, column=0, padx=10, pady=10)

        self.leave_lobby_btn = ctk.CTkButton(self.btns_frame, text="Leave Lobby", command=self.leave_lobby, font=("Verdana Arial", 14, "bold"), height=60, fg_color="green")
        self.leave_lobby_btn.grid(row=4, column=0, padx=10, pady=10)

        self.exit_game_btn = ctk.CTkButton(self.btns_frame, text="Exit Game", command=self.exit_game, font=("Verdana Arial", 14, "bold"), height=60, fg_color="green")
        self.exit_game_btn.grid(row=5, column=0, padx=10, pady=10)

    def show_rooms(self):
        for widget in self.room_list_frame.winfo_children():
            widget.destroy()

        self.room_buttons.clear()        
        self.join_btn.configure(state="disabled")

        
        response = requests.get(f"{SERVER_URL}/list_rooms")
        rooms = response.json()

        if not rooms:
            ctk.CTkLabel(self.room_list_frame, text="No rooms available").grid(row=0, column=0, pady=10, padx=10)
            return
        

        for index, room in enumerate(rooms):
            room_name = room["room_name"]
            host_name = room["host_player"]
            status = room["status"]
            response = requests.get(f"{SERVER_URL}/list_players_in_room", params={"room_name": room_name})
            players = response.json()
            nmb_players = len(players)
            text = f"{room_name} | ({status}) | Host: {host_name} | Players:{nmb_players}/6"

            btn = ctk.CTkButton(
            self.room_list_frame,
            text=text,
            anchor="w",
            width=260
        )
            btn.configure(command=lambda rn=room_name, b=btn: self.select_room(rn, b))
            btn.grid(row=index, column=0, padx=5, pady=3, sticky="ew")
            self.room_buttons.append(btn)

    def select_room(self, room_name, selected_button):
        self.selected_room_name = room_name
        for btn in self.room_buttons:
            btn.configure(fg_color="red")
        selected_button.configure(fg_color="green")
        response = requests.get(f"{SERVER_URL}/get_room", params={"room_name": self.selected_room_name})
        room = response.json()
        if room["host_player"] == self.player_name:            
            self.join_btn.configure(state="disabled", fg_color="#800000")
        elif room["host_player"] != self.player_name:            
            self.join_btn.configure(state="normal", fg_color="green")
        response = requests.get(f"{SERVER_URL}/list_players_in_room", params={"room_name": self.selected_room_name})
        players = response.json()
        if len(players) >= 2:
            self.start_game_btn.configure(state="normal", fg_color="green")

    def join_selected_room(self):
        if not self.selected_room_name:
            mb.showwarning("No room selected", "Please select a room to join.")
            return
        
        response = requests.get(f"{SERVER_URL}/get_room", params={"room_name": self.selected_room_name})
        room = response.json()        
        if not room:
            mb.showerror("Room not found", "This room does not exist.")
            self.show_rooms()
            return
        
        mb.showinfo("Joining Room", f"You are joining: {self.selected_room_name}")
        requests.post(f"{SERVER_URL}/join_room", params={"player_name": self.player_name, "room_name": self.selected_room_name})


    def start_game(self):
        response = requests.get(f"{SERVER_URL}/get_player", params={"player_name": self.player_name})
        player = response.json()        
        joined_room = player["joined_room"]
        requests.post(f"{SERVER_URL}/start_game", params={"req": joined_room})

        self.grid_forget()

               
        self.mp_game_screen = MultiplayerGameScreen(self.parent, None)
        self.mp_game = LocalMultiplayerGame(self.mp_game_screen, self.player_name, joined_room)
        self.mp_game_screen.mp_game = self.mp_game
        
    

    def leave_lobby(self):        
        requests.post(f"{SERVER_URL}/disconnect", params={"player_name": self.player_name})
        self.parent.protocol("WM_DELETE_WINDOW", self.parent.destroy)

        self.grid_forget()
        self.parent.initialize_main_menu()

    def on_app_close(self):
        try:
            requests.post(f"{SERVER_URL}/disconnect", params={"player_name": self.player_name})
        except Exception as e:
            print("Cleanup failed:", e)

    def exit_game(self):
        self.quit()

    def create_room_button_press(self):
        room_name = sd.askstring("Create Room", "Enter room name:")        
        if room_name:
            room_req = RoomCreateRequest(room_name=room_name, host_player_name=self.player_name)            
            create_room(room_req)        
            mb.showinfo("Room Created", f"Room '{room_name}' created.")
            self.show_rooms()