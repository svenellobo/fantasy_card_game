from deck import Deck
from player import Player
from discard_area import DiscardArea
import random
from constants import SERVER_URL
import requests

class LocalMultiplayerGame():
    def __init__(self, player_names: list[str], mp_game_screen, player_name, room_name):
        self.image_paths = []               
        self.deck = Deck()
        for card in self.deck.cards:
            self.image_paths.append(card.image)
        self.discard_area = DiscardArea()
        self.deck.shuffle_deck()
        self.players: dict[str, Player] = {}
        self.player_name = player_name
        self.room_name = room_name
        self.server_url = SERVER_URL
        
        self.turn_order = player_names.copy()
        random.shuffle(self.turn_order)
        self.current_player_index = 0
        self.mp_game_screen = mp_game_screen  

        self.card_taken = False
        self.card_discarded = False      

        for name in self.turn_order:
            player = Player()
            player.deal_hand(self.deck)
            self.players[name] = player

    

    def take_card_from_discard(self, card):
        if self.current_player == self.player_name and not self.card_taken:
            
            self.discard_area.discard_area_cards.remove(card)
            self.current_player.cards_in_hand.append(card)        
            self.mp_game_screen.display_cards(self.current_player.cards_in_hand, "player_hand")
            self.mp_game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.mp_game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.mp_game_screen.draw_button.configure(fg_color="#800000", state="disabled")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.current_player == self.player_name and not self.card_taken:        
            response = requests.post(f"{self.server_url}/draw_card", params={"room_name": self.room_name, "player_name":self.player_name})
            self.current_player.cards_in_hand.append(card)        
            self.mp_game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.mp_game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.card_taken = True
            self.mp_game_screen.draw_button.configure(fg_color="#800000", state="disabled")        
        
            
        
    def discard_from_hand(self, card):
        if self.card_taken and not self.card_discarded:            
            self.current_player.cards_in_hand.remove(card)
            self.discard_area.discard_area_cards.append(card)
            card.reset()
            self.mp_game_screen.display_cards(self.current_player.cards_in_hand, "player_hand")
            self.mp_game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_discarded = True
            if len(self.discard_area.discard_area_cards) < 10:
                self.mp_game_screen.end_turn_btn.configure(fg_color="green", state="normal")            
                self.mp_game_screen.status_area_lbl.configure(text="END TURN: Click on the 'End Turn' button")
            else:
                self.mp_game_screen.end_turn_btn.configure(fg_color="green", state="normal", text="End Game")
                self.mp_game_screen.status_area_lbl.configure(text="END GAME: Click on the 'End Game' button")
              
        
    def end_game(self):
        if any(card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes", "Island"} for card in self.player1.cards_in_hand):
            self.game_screen.open_choice_screen(self.player1, self.player2, self.discard_area)
        else:       
            self.game_screen.open_score_screen(self.player1, self.player2, self.discard_area) 
            
            
        
        
    
    def end_turn(self):
        self.game_screen.end_turn_btn.configure(state="disabled", fg_color="#800000")        
        if len(self.discard_area.discard_area_cards) >= 10:
            self.end_game()
        else: 
            if self.current_player == "player":                
                self.current_player = "cpu"
                self.game_screen.after(500, self.cpu_turn_logic)                
            elif self.current_player == "cpu":                                
                self.current_player = "player"
                self.player_turn_logic()
                
    
    def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):               
        self.current_player = "player"
        self.game_screen.end_turn_btn.configure(fg_color="#800000", state="disabled")
        self.game_screen.draw_button.configure(fg_color="green", state="normal")
        self.game_screen.status_area_lbl.configure(text="DRAW PHASE: Draw from the deck or double-click a discard area card to take it.")
        self.card_taken = False
        self.card_discarded = False
    

    

        
        
        