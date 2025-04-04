import customtkinter as ctk
from screens.card_widget import CardWidget


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.init_screen()
        
        
    def display_cards(self, hand, player=True):
        if player:
            col = 0
            for card in hand:            
                card_widget = CardWidget(self.hand_frame, card.image)
                card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")            
                col += 1
        else:
            col = 0
            for card in hand:            
                card_widget = CardWidget(self.opponent_frame, card.image)
                card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")            
                col += 1
        
        
    def init_screen(self):        
        
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)  
        self.columnconfigure(0, weight=0, minsize=150)
        self.columnconfigure(1, weight=0)
        
        self.draw_deck = ctk.CTkLabel(self, text="", height=220, width=150, fg_color="yellow")
        self.draw_deck.grid(row=1, column=0, sticky="ew", padx=40, pady=40)
        
        self.opponent_frame = ctk.CTkFrame(self, height=100, fg_color="green") 
        self.opponent_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)  
        
        self.discard_area = ctk.CTkFrame(self, height=500, fg_color="red") 
        self.discard_area.grid(row=1, column=1, sticky="ew", padx=10, pady=10) 
        
        self.hand_frame = ctk.CTkFrame(self, height=100, fg_color="blue") 
        self.hand_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        
        
        
    def back_to_menu(self):        
        self.grid_forget()  
        self.parent.initialize_main_menu()  
        