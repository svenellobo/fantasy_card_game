import customtkinter as ctk
from gui.lobby_screen import LobbyScreen
import tkinter.messagebox as mb
from database import add_player, get_player

class MpNameScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.player_name = None
        self.init_screen()

    def init_screen(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0) 
        self.grid_columnconfigure(2, weight=1)
        


        self.name_input_area = ctk.CTkFrame(self, width=900, height=600, fg_color="#6D4C41")
        self.name_input_area.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")

        self.name_input_lbl = ctk.CTkLabel(self.name_input_area, text="Enter you username:", fg_color="#2B2B2B", font=("Verdana Arial", 24, "bold"), justify="left", text_color="orange")
        self.name_input_lbl.grid(row=0, column=0, pady=15, padx=55, sticky="nsew")

        self.input_name_box = ctk.CTkEntry(self.name_input_area, placeholder_text="Enter you username here", height=40, width=200, font=("Verdana Arial", 16, "bold"), state="normal")
        self.input_name_box.grid(row=1, column=0, pady=25, padx=55, sticky="nsew")

        self.enter_btn = ctk.CTkButton(self.name_input_area, fg_color="green", state="normal",
                                         text="Enter", font=("Verdana Arial", 14, "bold"), height=50, command=lambda: self.enter_multiplayer())
        self.enter_btn.grid(row=2, column=0, padx=10, pady=10)


    def enter_multiplayer(self):        
        self.player_name = self.input_name_box.get().strip()
        if not self.player_name:
            mb.showwarning(title="No Username", message="Please enter your username")
            return

        if get_player(self.player_name):
            mb.showerror(title="Name Taken", message="This username is already in use. Please choose another one.")
            return
        
        else:
            add_player(self.player_name)
            self.lobby_screen = LobbyScreen(self.parent, self.player_name)
            self.grid_remove()