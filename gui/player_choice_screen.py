import customtkinter as ctk
from gui.card_widget import CardWidget
from constants import ALL_SUITS

class PlayerChoiceScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2, discard_area):
        super().__init__(parent)        
        self.player1 = player1
        self.player2 = player2
        self.discard_area = discard_area
        self.cards_with_choice = []
        
        for card in self.player1.cards_in_hand:
            if card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes"}:
                self.cards_with_choice.append(card)
                
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        
        self.init_screen()
        
    def init_screen(self):       
        
        self.left_column = ctk.CTkFrame(self, fg_color="green")
        self.left_column.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player_choice_area = ctk.CTkFrame(self, fg_color="purple")
        self.player_choice_area.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.right_column = ctk.CTkFrame(self, fg_color="green")
        self.right_column.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        #self.player_choice_area.grid_columnconfigure(0, weight=1)
        #self.player_choice_area.grid_columnconfigure(1, weight=1) 
        #self.player_choice_area.grid_rowconfigure(0, weight=1)
        #self.player_choice_area.grid_rowconfigure(1, weight=1)
        #self.player_choice_area.grid_rowconfigure(2, weight=1)
        
        self.player1_choice_lbl = ctk.CTkLabel(self.player_choice_area, text=f"Card options")
        self.player1_choice_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=7, sticky="nsew")
        
        
        col = 0
        
        for card in self.cards_with_choice:
            card_widget = CardWidget(self.player_choice_area, card.image, card, click_action=lambda c=card: self.player_choice(c) )
            card_widget.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            
            
        self.choice_area_frame = ctk.CTkFrame(self, fg_color="green")
        self.choice_area_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        
        
    def player_choice(self, card):
        for widget in self.choice_area_frame.winfo_children():
            widget.destroy()
            
        if card.original_state["name"] == "Mirage":
            col = 0
            row = 0
            for key,values in card.mirage_suits.items():
                for value in values:
                    self.btn_option = ctk.CTkButton(self.choice_area_frame, fg_color="blue", text=f"{key}: {value}", height=60)
                    self.btn_option.grid(row=row, column=col, sticky="ew", padx=10, pady=5)
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1
                
        elif card.original_state["name"] == "Shapeshifter":
            col = 0
            row = 0
            for key,values in card.shape_suits.items():
                for value in values:
                    self.btn_option = ctk.CTkButton(self.choice_area_frame, fg_color="blue", text=f"{key}: {value}", height=60)
                    self.btn_option.grid(row=row, column=col, sticky="ew", padx=10, pady=5)
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1
                        
        elif card.original_state["name"] == "Doppelganger":
            col = 0
            for dop_card in self.player1.cards_in_hand:
                card_widget = CardWidget(self.choice_area_frame, card.image, dop_card)
                card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
                col += 1
                
        elif card.original_state["name"] == "Book of Changes":
            col = 0
            for boc_card in self.player1.cards_in_hand:
                card_widget = CardWidget(self.choice_area_frame, boc_card.image, boc_card)
                card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
                col += 1 
            for suit in ALL_SUITS:
                pass
                
        elif card.original_state["name"] == "Necromancer":
            col = 0
            row = 0
            for disc_card in self.discard_area.discard_area_cards:
                if disc_card.suit in card.discard_suits:
                    print(card)
                    print(disc_card)
                    card_widget = CardWidget(self.choice_area_frame, disc_card.image, disc_card)
                    card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    col += 1
                    if col >= 5:
                        col = 0
                        row = 1
    
            
            
        
        