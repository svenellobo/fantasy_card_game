import customtkinter as ctk
from gui.card_widget import CardWidget
from constants import ALL_SUITS
from gui.score_screen import ScoreScreen

class PlayerChoiceScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2, discard_area):
        super().__init__(parent) 
        self.parent = parent       
        self.player1 = player1
        self.player2 = player2
        self.discard_area = discard_area
        self.cards_with_choice = []
        
        
        
        
        for card in self.player1.cards_in_hand:
            if card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes"} and not card.is_blanked:
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
        
        self.right_column.grid_rowconfigure(0, weight=1)
        self.right_column.grid_columnconfigure(0, weight=1)
        
        self.to_score_screen_btn = ctk.CTkButton(self.right_column, fg_color="blue",
                                                 text="To Score Screen", height=60, command=self.open_score_screen)
        self.to_score_screen_btn.grid(row=0, column=0, padx=5, pady=5)
        
        
        
        self.player1_choice_lbl = ctk.CTkLabel(self.player_choice_area, text=f"Card options")
        self.player1_choice_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=7, sticky="nsew")
        
        
        col = 0
        
        for card in self.cards_with_choice:
            card_widget = CardWidget(self.player_choice_area, card.image, card, click_action=lambda c=card: self.player_choice(c))
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
                    self.btn_option = ctk.CTkButton(self.choice_area_frame, fg_color="blue", text=f"{key}: {value}",
                                                    height=60, command=lambda k=key, v=value: self.mirage_shapeshift_choice(card, k, v))
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
                    self.btn_option = ctk.CTkButton(self.choice_area_frame, fg_color="blue", text=f"{key}: {value}",
                                                    height=60, command=lambda k=key, v=value: self.mirage_shapeshift_choice(card, k, v))
                    self.btn_option.grid(row=row, column=col, sticky="ew", padx=10, pady=5)
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1
                        
        elif card.original_state["name"] == "Doppelganger":
            col = 0
            row = 0
            """for dop_card in self.player1.cards_in_hand:
                card_widget = CardWidget(self.choice_area_frame, dop_card.image, dop_card,
                                         click_action=lambda c=card, dop_c=dop_card: self.doppelganger_choice(c, dop_c))
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                col += 1
                if col >= 5:
                    col = 0
                    row += 1
                    print(card)
                    print(dop_card)"""
                    
            for dop_card in self.player1.cards_in_hand:
                self.create_card_widget(card, dop_card, row, col)
                col += 1
                if col >= 5:
                    col = 0
                    row += 1
                
        elif card.original_state["name"] == "Book of Changes":
            col = 0
            row = 0
            self.chosen_card = None
            for boc_card in self.player1.cards_in_hand:
                card_widget = CardWidget(self.choice_area_frame, boc_card.image, boc_card,
                                         click_action=lambda b=boc_card: self.set_chosen_card(b))
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                col += 1 
                if col >= 5:
                    col = 0
                    row += 1
                    
            suit_col = 0
            suit_row = 0
            self.suits_area = ctk.CTkFrame(self.choice_area_frame, fg_color="yellow")
            self.suits_area.grid(row=0, column=6, sticky="ew", padx=10, pady=5)
            for suit in ALL_SUITS:
                self.btn_option = ctk.CTkButton(self.suits_area, fg_color="blue", text=f"{suit}",
                                                height=40, command=lambda s=suit: self.book_of_changes_choices(self.chosen_card, s))
                self.btn_option.grid(row=suit_row, column=suit_col, sticky="ew", padx=10, pady=5)
                suit_col += 1
                if suit_col >= 3:
                    suit_col = 0
                    suit_row += 1
                
        elif card.original_state["name"] == "Necromancer":
            self.card_picked = False
            col = 0
            row = 0
            for disc_card in self.discard_area.discard_area_cards:
                if disc_card.suit in card.discard_suits:                    
                    card_widget = CardWidget(self.choice_area_frame, disc_card.image,
                                             disc_card, click_action=self.necromancer_choice)
                    card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    col += 1
                    if col >= 5:
                        col = 0
                        row = 1
    
    
    
        
    def create_card_widget(self, card, dop_card, row, col):
        card_widget = CardWidget(
            self.choice_area_frame,
            dop_card.image,
            dop_card,
            click_action=lambda event: self.doppelganger_choice(card, dop_card)  
        )
        card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
           
            
    def mirage_shapeshift_choice(self, card, suit, value):
        card.suit = suit
        card.name = value
        print(card) 
        
    def doppelganger_choice(self, card, dop_card):
        
        print(f"doppelganger: {card}")
        print(f"original card: {dop_card}")
        card.name = dop_card.name
        card.base_power = dop_card.base_power
        card.suit = dop_card.suit
        card.best_card = dop_card       
        print(f"changed card: {card}")
        print(f"original card: {dop_card}")
        
        
    def book_of_changes_choices(self, chosen_card, suit):
        if chosen_card:
            chosen_card.suit = suit
            print(chosen_card)
        
        
    def set_chosen_card(self, card):
        self.chosen_card = card
        print(self.chosen_card)
        
    def necromancer_choice(self, card):
        if not self.card_picked:
            self.player1.cards_in_hand.append(card)
            self.discard_area.discard_area_cards.remove(card)
            self.card_picked = True
            print(card)
            
    def open_score_screen(self):        
        self.destroy()        
        score_screen = ScoreScreen(self.parent, self.player1, self.player2)
        score_screen.grid(row=0, column=0, sticky="nsew")