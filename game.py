from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea
from gui.game_screen import GameScreen
from gui.card_widget import CardWidget
from gui.score_screen import ScoreScreen
from card_library.beast.dragon import Dragon




class Game():
    def __init__(self, game_screen):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = Player()
        self.player2 = CPUPlayer()
        self.discard_area = DiscardArea()
        self.current_player = None
        self.card_taken = False
        self.card_discarded = False        
        self.game_screen = game_screen    
        
        dragon = Dragon()
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
           

        self.play()
            
        
    def take_card_from_discard(self, card):
        if not self.card_taken:        
            self.discard_area.discard_area_cards.remove(card)
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on a card in hand to discard it")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.current_player == "player" and not self.card_taken:        
            card = self.deck.draw_card()
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on an unwanted card in your hand to discard it.")
            self.card_taken = True
        else:
            print("already drew")
            
        
    def discard_from_hand(self, card):
        if self.card_taken and not self.card_discarded:            
            self.player1.cards_in_hand.remove(card)
            self.discard_area.discard_area_cards.append(card)
            card.reset()
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_discarded = True
            self.game_screen.end_turn_btn.configure(fg_color="green", state="normal")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on the 'End Turn' button")
            
            
            
        
    def end_game(self):
        print("game ended")
        #p1_score = self.player1.calculate_total_points()
        #p2_score = self.player2.calculate_total_points()
        self.game_screen.open_score_screen(self.player1, self.player2)
        
        
            
            
        
        
    
    def end_turn(self):
        if self.card_taken and self.card_discarded:
            if len(self.discard_area.discard_area_cards) >= 10:
                self.end_game()
            else: 
                if self.current_player == "player":                
                    self.current_player = "cpu"
                    self.game_screen.after(1000, self.cpu_turn_logic())                
                elif self.current_player == "cpu":                
                    self.current_player = "player"
                    self.player_turn_logic()
                
    
    def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):
        print("Player 1's turn...")
        self.current_player = "player"
        self.game_screen.end_turn_btn.configure(fg_color="red", state="disabled")
        self.game_screen.status_area_lbl.configure(text="HINT: Draw a card from the deck or take one from the discard area.")
        self.card_taken = False
        self.card_discarded = False      
        
        
                
                
    def cpu_turn_logic(self):
        print("CPU Player's turn...")
        self.player2.take_turn(self.deck, self.discard_area.discard_area_cards)
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
        self.end_turn()
        
            
    
    

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck) 
        self.update_game_screen()
        
        self.player_turn_logic()
        
        
        """ while not self.is_game_over(self.discard_area.discard_area_cards):
            self.player_turn_logic()
            
            if self.is_game_over(self.discard_area.discard_area_cards):  
                break
                
            self.cpu_turn_logic()
            if self.is_game_over(self.discard_area.discard_area_cards):  
                break"""
        
        
        """for card in self.player1.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player1.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
                
        for card in self.player2.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player2.cards_in_hand, discard_area=self.discard_area.discard_area_cards)"""
        
                
        
        """player1_score = self.player1.calculate_total_points(self.player1.cards_in_hand) 
        player2_score = self.player2.calculate_total_points(self.player2.cards_in_hand)
        print(f"Player 1 Score: {player1_score}") 
        print(f"Player 2 Score: {player2_score}") """
    
    
        #draw a card
        #select a card to discard
        #table list append card that's discarded
        #player 2 turn
        #draw a card or take one from table
        #analyze cards on a table and if value added is >= 25 takes that card from table
        #remove worst card    
            
    
        

    