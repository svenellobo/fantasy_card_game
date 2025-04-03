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
        """self.menu_label = ctk.CTkLabel(self, text="Welcome to Fantasy Realms!", text_color="green", font=("Arial", 24))
        self.menu_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.start_button = ctk.CTkButton(self, text="Start Game", command=self.back_to_menu)
        self.start_button.grid(row=1, column=0, padx=20, pady=10)"""
        
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)  
        self.columnconfigure(0, weight=1)
        
        self.opponent_frame = ctk.CTkFrame(self, height=100, fg_color="green") 
        self.opponent_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)  
        
        self.discard_area = ctk.CTkFrame(self, height=500, fg_color="red") 
        self.discard_area.grid(row=1, column=0, sticky="ew", padx=10, pady=10) 
        
        self.hand_frame = ctk.CTkFrame(self, height=100, fg_color="blue") 
        self.hand_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        
        
        
    def back_to_menu(self):        
        self.grid_forget()  
        self.parent.initialize_main_menu()  
        