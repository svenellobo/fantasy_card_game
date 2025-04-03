import customtkinter as ctk
from screens.game_screen import GameScreen
from game import Game

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
        self.menu_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.start_button = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=1, column=0, padx=20, pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.quit_game)
        self.exit_button.grid(row=1, column=1, padx=20, pady=10)
        
        
    def start_game(self):
        print("Game starting...")
        self.grid_forget()        
        self.game_screen = GameScreen(self.parent)
        self.game = Game(self.game_screen)
        
    def quit_game(self):
        print("Game quitting...")