import customtkinter as ctk
from database import list_rooms, get_room, update_room_status, delete_room, remove_player, update_player_joined_room
from tkinter import messagebox as mb


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

        self.create_btn = ctk.CTkButton(self.btns_frame, text="Create Room")
        self.create_btn.grid(row=0, column=0, padx=10, pady=10)

        self.join_btn = ctk.CTkButton(self.btns_frame, text="Join Room")
        self.join_btn.grid(row=1, column=0, padx=10, pady=10)

        self.refresh_btn = ctk.CTkButton(self.btns_frame, text="Refresh")
        self.refresh_btn.grid(row=2, column=0, padx=10, pady=10)

        self.delete_room_btn = ctk.CTkButton(self.btns_frame, text="Delete Room")
        self.delete_room_btn.grid(row=3, column=0, padx=10, pady=10)

        self.start_game_btn = ctk.CTkButton(self.btns_frame, text="Start Game")
        self.start_game_btn.grid(row=4, column=0, padx=10, pady=10)

        self.leave_lobby_btn = ctk.CTkButton(self.btns_frame, text="Leave Lobby", command=self.leave_lobby)
        self.leave_lobby_btn.grid(row=5, column=0, padx=10, pady=10)

    def show_rooms(self):
        for widget in self.room_list_frame.winfo_children():
            widget.destroy()

        self.room_buttons.clear()        
        self.join_btn.configure(state="disabled")

        rooms = list_rooms()

        if not rooms:
            ctk.CTkLabel(self.room_list_frame, text="No rooms available").grid(row=0, column=0, pady=10, padx=10)
            return

        for index, room in enumerate(rooms):
            room_name = room[1]
            host_name = room[2]
            status = room[3]
            text = f"{room_name} ({status}) Host:{host_name}"

            btn = ctk.CTkButton(
            self.room_list_frame,
            text=text,
            anchor="w",
            width=260,
            command=lambda rn=room_name, b=btn: self.select_room(rn, b) 
        )
            btn.grid(row=index, column=0, padx=5, pady=3, sticky="ew")
            self.room_buttons.append(btn)

    def select_room(self, room_name, selected_button):
        self.selected_room_name = room_name
        for btn in self.room_buttons:
            btn.configure(fg_color="red")
        selected_button.configure(fg_color="green")
        self.join_btn.configure(state="normal")

    def join_selected_room(self):
        if not self.selected_room_name:
            mb.showwarning("No room selected", "Please select a room to join.")
            return
        
        room = get_room(self.selected_room_name)
        if not room:
            mb.showerror("Room not found", "This room does not exist.")
            self.show_rooms()
            return
        
        mb.showinfo("Joining Room", f"You are joining: {self.selected_room_name}")
        update_player_joined_room(room[1], self.player_name)
        

    def start_game(self):
        update_room_status(self.selected_room_name, "in_progress")
        #tu pokrenuti multiplayer game screen

    def delete_room(self):
        delete_room(self.selected_room_name)
        mb.showinfo("Room Deleted", "The room has been deleted.")
        self.show_rooms()

    def leave_lobby(self):
        remove_player(self.player_name)
        self.parent.protocol("WM_DELETE_WINDOW", self.parent.destroy)

        self.grid_forget()
        self.parent.initialize_main_menu()

    def on_app_close(self):
        try:
            remove_player(self.player_name)
        except Exception as e:
            print("Cleanup failed:", e)