from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea
from gui.game_screen import GameScreen
from gui.card_widget import CardWidget
from gui.score_screen import ScoreScreen
import random




class Game():
    def __init__(self, game_screen): 
        self.image_paths = []       
        self.deck = Deck()
        for card in self.deck.cards:
            self.image_paths.append(card.image)
        self.deck.shuffle_deck()
        self.discard_area = DiscardArea()
        self.player1 = Player()
        self.player2 = CPUPlayer()
        self.player2.discard_area = self.discard_area.discard_area_cards
        
        self.current_player = random.choice(["player", "cpu"])
        self.card_taken = False
        self.card_discarded = False        
        self.game_screen = game_screen 

        self.play()
            
        
    def take_card_from_discard(self, card):
        if self.current_player == "player" and not self.card_taken:        
            self.discard_area.discard_area_cards.remove(card)
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.game_screen.draw_button.configure(fg_color="#800000", state="disabled")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.current_player == "player" and not self.card_taken:        
            card = self.deck.draw_card()
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.card_taken = True
            self.game_screen.draw_button.configure(fg_color="#800000", state="disabled")
        
        
            
        
    def discard_from_hand(self, card):
        if self.card_taken and not self.card_discarded:            
            self.player1.cards_in_hand.remove(card)
            self.discard_area.discard_area_cards.append(card)
            card.reset()
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_discarded = True
            if len(self.discard_area.discard_area_cards) < 10:
                self.game_screen.end_turn_btn.configure(fg_color="green", state="normal")            
                self.game_screen.status_area_lbl.configure(text="END TURN: Click on the 'End Turn' button")
            else:
                self.game_screen.end_turn_btn.configure(fg_color="green", state="normal", text="End Game")
                self.game_screen.status_area_lbl.configure(text="END GAME: Click on the 'End Game' button")
              
        
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
         
        
        
                
                
    def cpu_turn_logic(self):               
        disc_len = len(self.discard_area.discard_area_cards)        
        turn_logic = self.player2.take_turn(self.deck, self.discard_area.discard_area_cards)                
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
        if disc_len == len(self.discard_area.discard_area_cards):
            self.game_screen.card_preview(turn_logic.image) 
            self.game_screen.card_preview_info.configure(text="Opponent took this card from the discard area:")     
               
        self.end_turn()
        
            
    
    

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck) 
        self.update_game_screen()
        if self.current_player == "player":
            self.game_screen.show_temporary_discard_message("You’re going first.") 
            self.player_turn_logic()
        else:
            self.game_screen.draw_button.configure(fg_color="#800000", state="disabled")
            self.game_screen.end_turn_btn.configure(state="disabled", fg_color="#800000")
            self.game_screen.status_area_lbl.configure(text="OPPONENT's TURN")
            self.game_screen.show_temporary_discard_message("Your opponent goes first.")             
            self.game_screen.after(5000, self.cpu_turn_logic)
        
             
   