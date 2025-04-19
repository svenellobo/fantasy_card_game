import customtkinter as ctk

class PlayerChoiceScreen(ctk.CTkFrame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.game = game
        self.init_screen()
        
    def init_screen(self):
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)  
        self.columnconfigure(0, weight=0, minsize=150)
        self.columnconfigure(1, weight=0)