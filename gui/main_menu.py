import customtkinter as ctk
from gui.game_screen import GameScreen
from game import Game
from gui.instructions import Instructions

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid()
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.init_screen()
    
    
    def init_screen(self):
        self.menu_label = ctk.CTkLabel(self, text="Welcome to Fantasy Realms!", text_color="red", font=("Arial", 24))
        self.menu_label.grid(row=0, column=0, columnspan=3, pady=20)
        
        self.start_button = ctk.CTkButton(self, text="Start Game", font=("Georgia", 14, "bold"), command=self.start_game, height=60, fg_color="green")
        self.start_button.grid(row=1, column=0, padx=20, pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", font=("Georgia", 14, "bold"), command=self.quit_game, height=60, fg_color="#800000")
        self.exit_button.grid(row=1, column=2, padx=20, pady=10)
        
        self.instructions_button = ctk.CTkButton(self, text="How to Play", font=("Georgia", 14, "bold"), command=self.how_to_play, height=60, fg_color="green")
        self.instructions_button.grid(row=1, column=1, padx=20, pady=10)
        
        
    def start_game(self):
        print("Game starting...")
        self.grid_forget()        
        self.game_screen = GameScreen(self.parent, None)
        self.game = Game(self.game_screen)
        self.game_screen.game = self.game
        
        
    def quit_game(self):
        print("Game quitting...")
        
    def how_to_play(self):
        self.instruction = Instructions(self.parent)
        self.instruction.grid(row=0, column=0, sticky="nsew")