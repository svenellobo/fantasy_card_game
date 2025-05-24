import customtkinter as ctk
from gui.card_widget import CardWidget
from constants import *
from gui.score_screen import ScoreScreen
from gui.cards_in_hand_screen import CardsInHandScreen
from gui.card_library import CardLibrary

class PlayerChoiceScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2, discard_area, card_images):
        super().__init__(parent) 
        self.parent = parent       
        self.player1 = player1
        self.player2 = player2
        self.hand_images = []        
        self.discard_area = discard_area
        self.cards_with_choice = []
        self.configure(fg_color="#4E342E")
        self.necromancer_card = None
        self.boc_card = None
        self.boc_area = False
        self.necro_card_picked = False
        self.island_choice_picked = False
        self.library_open = False
        self.cards_in_hand_screen_open = False
        self.card_info_labels = {}
        self.image_paths = card_images
        
        
        for card in self.player1.cards_in_hand:
            self.hand_images.append(card.image)
            if card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes", "Island"}:
                self.cards_with_choice.append(card)
                
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        
        self.init_screen()
        
    def init_screen(self):       
        
        self.left_column = ctk.CTkFrame(self, fg_color="#4E342E")
        self.left_column.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player_choice_area = ctk.CTkFrame(self, fg_color="#5D4037")
        self.player_choice_area.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        
        self.right_column = ctk.CTkFrame(self, fg_color="#4E342E")
        self.right_column.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        self.right_column.grid_rowconfigure(0, weight=1)
        self.right_column.grid_columnconfigure(0, weight=1)
        
        self.to_score_screen_btn = ctk.CTkButton(self.right_column, fg_color="#b7410e",
                                                 text="Proceed To Score Screen", height=60, font=("Georgia", 14, "bold"), command=self.open_score_screen)
        self.to_score_screen_btn.grid(row=0, column=0, padx=5, pady=5)    
        
        cards_in_hand_btn = ctk.CTkButton(self.right_column, fg_color="green",
                                          text="Cards in Hand", height=60, font=("Georgia", 14, "bold"), command=self.open_cards_in_hand_screen)
        cards_in_hand_btn.grid(row=1, column=0, padx=5, pady=5) 
        
        card_library_btn = ctk.CTkButton(self.right_column, fg_color="green",
                                          text="Card Library", height=60, font=("Georgia", 14, "bold"), command=self.open_card_library)
        card_library_btn.grid(row=2, column=0, padx=5, pady=5) 
        
        
        self.player1_choice_lbl = ctk.CTkLabel(self.player_choice_area, text=f"Double click on a card.", font=("Georgia", 16, "bold"), text_color="orange", fg_color="#2B2B2B")
        self.player1_choice_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=10, sticky="nsew")
        
        self.choice_area_frame = ctk.CTkFrame(self, fg_color="#6D4C41" ) 
        self.choice_area_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.choice_area_frame.grid_columnconfigure(0, weight=1)
        self.choice_area_frame.grid_columnconfigure(1, weight=1)
        
        self.instruction_area = ctk.CTkFrame(self.choice_area_frame, fg_color="#2B2B2B" ) 
        self.instruction_area.grid(row=0, column=0, padx=5, pady=(25,0))
        
        self.center_frame = ctk.CTkFrame(self.choice_area_frame, fg_color="transparent") 
        self.center_frame.grid(row=1, column=0, padx=0, pady=(15,0), sticky="n")        
        
        
        self.instruction_area_lbl = ctk.CTkLabel(self.instruction_area, text="", font=("Georgia", 14, "bold"))
        self.instruction_area_lbl.grid(row=0, column=0, padx=5, pady=5)
         
        
        
        col = 1        
        for card in self.cards_with_choice:
            card_widget = CardWidget(self.player_choice_area, card.image, card,
                                     click_action=lambda c=card: self.player_choice(c))            
            card_widget.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")
            card_info_area = ctk.CTkLabel(self.player_choice_area,
                                               text="",
                                               text_color="green",
                                               fg_color="#2B2B2B",
                                               font=("Georgia", 14))
            card_info_area.grid(row=2, column=col, padx=5, pady=5)
            self.card_info_labels[card] = (card_info_area, card_widget)
            col += 1
            
        self.player_choice_area.grid_columnconfigure(0, weight=1)
        self.player_choice_area.grid_columnconfigure(1, weight=0)
        self.player_choice_area.grid_columnconfigure(2, weight=0)
        self.player_choice_area.grid_columnconfigure(3, weight=0)
        self.player_choice_area.grid_columnconfigure(4, weight=0)
        self.player_choice_area.grid_columnconfigure(5, weight=0)
        self.player_choice_area.grid_columnconfigure(6, weight=0)
        self.player_choice_area.grid_columnconfigure(7, weight=1)
        
        
            
            
        
        
        
        
    def player_choice(self, card):
        for widget in self.center_frame.winfo_children():
            widget.destroy()
        if self.boc_area:
            self.suits_area.destroy()
            self.boc_area = False  
            
            
        if card.original_state["name"] == "Mirage":
            col = 0
            row = 0
            for key,values in card.mirage_suits.items():
                suit_lbl = ctk.CTkLabel(self.center_frame, text=f"{key}:", fg_color="#2B2B2B", font=("Georgia", 14, "bold"))
                suit_lbl.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
                for value in values:
                    self.btn_option = ctk.CTkButton(self.center_frame, fg_color="#B7410E", text=f"{value}", font=("Georgia", 14),
                                                    height=60, command=lambda k=key, v=value: self.mirage_shapeshift_choice(card, k, v))
                    self.btn_option.grid(row=row, column=col+1, sticky="ew", padx=10, pady=5)
                    
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1
            self.instruction_area_lbl.configure(text="Select a card for 'Mirage' to duplicate.")
                
        elif card.original_state["name"] == "Shapeshifter":
            col = 0
            row = 0
            for key,values in card.shape_suits.items():
                suit_lbl = ctk.CTkLabel(self.center_frame, text=f"{key}:", fg_color="#2B2B2B", font=("Georgia", 14, "bold"))
                suit_lbl.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
                for value in values:
                    self.btn_option = ctk.CTkButton(self.center_frame, fg_color="#B7410E", text=f"{value}", font=("Georgia", 14),
                                                    height=60,
                                                    command=lambda k=key, v=value: self.mirage_shapeshift_choice(card, k, v))
                    self.btn_option.grid(row=row, column=col+1, sticky="ew", padx=10, pady=5)
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1
            self.instruction_area_lbl.configure(text="Select a card for 'Shapeshifter' to duplicate.")
                        
        elif card.original_state["name"] == "Doppelganger":
            col = 0
            row = 0
            for dop_card in self.player1.cards_in_hand:
                self.create_card_widget(card, dop_card, row, col)
                col += 1
                if col >= 5:
                    col = 0
                    row += 1
            self.instruction_area_lbl.configure(text="Double click on a card for 'Doppelganger' to duplicate.")
                
        elif card.original_state["name"] == "Book of Changes":
            self.boc_card_picked = False
            col = 1
            row = 0
            self.chosen_card = None
            self.boc_area = True
            self.boc_card = card
            for boc_card in self.player1.cards_in_hand:
                card_widget = CardWidget(self.center_frame, boc_card.image, boc_card,
                                         click_action=lambda b=boc_card: self.set_chosen_card(b))
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                col += 1
                if col >= 5:
                    col = 1
                    row += 1 
                
                    
            suit_col = 1
            suit_row = 1
            self.suits_area = ctk.CTkFrame(self.choice_area_frame, fg_color="#6D4C41") 
            self.suits_area.grid(row=1, column=1, sticky="nsew", padx=0, pady=(25,0))
            
        
            
            self.suits_area.grid_columnconfigure(0, weight=1)
            self.suits_area.grid_columnconfigure(1, weight=0)
            self.suits_area.grid_columnconfigure(2, weight=0)
            self.suits_area.grid_columnconfigure(3, weight=1)
            
            
            
            self.instruction_area_lbl.configure(text="Double-click a card to select it, then choose a suit to change it to.")
            
            suits_area_lbl = ctk.CTkLabel(self.suits_area, fg_color="#2B2B2B", text="Suits:", font=("Georgia", 14, "bold"))
            suits_area_lbl.grid(row=0, column=1,  sticky="nsew", padx=10, pady=5, columnspan=2)
            
            for suit in ALL_SUITS:
                
                self.btn_option = ctk.CTkButton(self.suits_area, fg_color="#B7410E", text=f"{suit}",
                                                height=40, font=("Georgia", 14),
                                                command=lambda c=card, s=suit: self.book_of_changes_choices(c, self.chosen_card, s))
                self.btn_option.grid(row=suit_row, column=suit_col, sticky="ew", padx=5, pady=5)
                suit_col += 1
                if suit_col >= 3:
                    suit_col = 1
                    suit_row += 1
                
        elif card.original_state["name"] == "Necromancer":
            self.necromancer_card = card
            
            col = 0
            row = 0
            for disc_card in self.discard_area.discard_area_cards:
                if disc_card.suit in card.discard_suits:                    
                    card_widget = CardWidget(self.center_frame, disc_card.image,
                                             disc_card, click_action=self.necromancer_choice)
                    card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    col += 1
                    if col >= 5:
                        col = 0
                        row = 1
                        
            self.instruction_area_lbl.configure(text="Double click on a card from discard to add it to your hand.")
            
        elif card.original_state["name"] == "Island":
            
            col = 0
            row = 0
            for island_card in self.player1.cards_in_hand:
                if island_card.suit in {FLAME, FLOOD}:                    
                    card_widget = CardWidget(self.center_frame, island_card.image,
                                             island_card, click_action=lambda ic=island_card: self.island_choice(card, ic))
                    card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    col += 1
                    if col >= 5:
                        col = 0
                        row = 1
    
            self.instruction_area_lbl.configure(text="Double click on a card to clear its penalties.")
    
    
    
            
        
    def create_card_widget(self, card, dop_card, row, col):
        card_widget = CardWidget(
            self.center_frame,
            dop_card.image,
            dop_card,
            click_action=lambda event: self.doppelganger_choice(card, dop_card)  
        )
        card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
    def island_choice(self, card, island_card):
        if not self.island_choice_picked:
            island_card.has_penalty = False
            self.island_choice_picked = True
            if card in self.card_info_labels:
                card_info_area = self.card_info_labels[card][0]
                card_info_area.configure(text=f"{island_card.name}\n")
                card_widget = self.card_info_labels[card][1]
                card_widget.configure(border_color="blue") 
                card_widget.unbind("<Enter>")
                card_widget.card_label.unbind("<Enter>")
                card_widget.unbind("<Leave>")
                card_widget.card_label.unbind("<Leave>")
        
        
            
           
            
    def mirage_shapeshift_choice(self, card, suit, value):
        card.suit = suit
        card.name = value        
        if card in self.card_info_labels:
            card_info_area = self.card_info_labels[card][0]            
            card_info_area.configure(text=f"{card.name}\n{card.suit} suit") 
            card_widget = self.card_info_labels[card][1]
            card_widget.configure(border_color="blue") 
            card_widget.unbind("<Enter>")
            card_widget.card_label.unbind("<Enter>")
            card_widget.unbind("<Leave>")
            card_widget.card_label.unbind("<Leave>")
              
       
        
        
    def doppelganger_choice(self, card, dop_card):       
        card.name = dop_card.name
        card.base_power = dop_card.base_power
        card.suit = dop_card.suit
        card.best_card = dop_card 
        card_widget = self.card_info_labels[card][1]                
        if card in self.card_info_labels:
            card_info_area = self.card_info_labels[card][0]
            card_info_area.configure(text=f"{dop_card.name}\n{dop_card.suit} suit")
            card_widget.configure(border_color="green") 
            card_widget.unbind("<Enter>")
            card_widget.card_label.unbind("<Enter>")
            card_widget.unbind("<Leave>")
            card_widget.card_label.unbind("<Leave>")
                 
        
        
        
    def book_of_changes_choices(self, boc, chosen_card, suit):
        if not self.boc_card_picked:        
            if chosen_card:
                chosen_card.suit = suit            
                card_info_area_boc = self.card_info_labels[boc][0]
                self.boc_card_picked = True
                if chosen_card in self.cards_with_choice:
                    card_info_area_card = self.card_info_labels[chosen_card][0]
                    card_info_area_card.configure(text=f"{chosen_card.name}\n{suit} suit")
                card_info_area_boc.configure(text=f"{chosen_card.original_state['name']}\n{suit} suit")             
                card_widget = self.card_info_labels[boc][1]
                card_widget.configure(border_color="green") 
                card_widget.unbind("<Enter>")
                card_widget.card_label.unbind("<Enter>")
                card_widget.unbind("<Leave>")
                card_widget.card_label.unbind("<Leave>")
                
        
        
    def set_chosen_card(self, card):
        self.chosen_card = card
        card_info_area = self.card_info_labels[self.boc_card][0]
        card_info_area.configure(text=f"{card.original_state['name']}")        
        
    def necromancer_choice(self, card):
        if not self.necro_card_picked:
            self.player1.cards_in_hand.append(card)
            self.discard_area.discard_area_cards.remove(card)
            self.necro_card_picked = True
        if self.necromancer_card in self.card_info_labels:
            card_info_area = self.card_info_labels[self.necromancer_card][0]
            card_info_area.configure(text=f"{card.name}")
            card_widget = self.card_info_labels[self.necromancer_card][1]
            card_widget.configure(border_color="blue")
            card_widget.unbind("<Enter>")
            card_widget.card_label.unbind("<Enter>")
            card_widget.unbind("<Leave>")
            card_widget.card_label.unbind("<Leave>")
            
            
    def open_score_screen(self):        
        self.destroy()        
        score_screen = ScoreScreen(self.parent, self.player1, self.player2, self.discard_area)
        score_screen.grid(row=0, column=0, sticky="nsew")
        
    def open_cards_in_hand_screen(self):
        if not self.cards_in_hand_screen_open:
            self.cards_in_hand_screen_open = True
            self.cards_in_hand_screen = CardsInHandScreen(self.parent, self.hand_images)         
            self.cards_in_hand_screen.grid(row=0, column=0, sticky="nsew")
        else:
            self.cards_in_hand_screen.grid(row=0, column=0, sticky="nsew")
            
    def open_card_library(self):
        if not self.library_open:
            self.library_open = True
            self.card_library = CardLibrary(self.parent, self.image_paths)         
            self.card_library.grid(row=0, column=0, sticky="nsew")
        else:
            self.card_library.grid(row=0, column=0, sticky="nsew")
        
    