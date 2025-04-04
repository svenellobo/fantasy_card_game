from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea
from screens.game_screen import GameScreen
from screens.card_widget import CardWidget



class Game():
    def __init__(self, game_screen):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = CPUPlayer()
        self.player2 = CPUPlayer()
        self.discard_area = DiscardArea()
        self.game_screen = game_screen
        
        self.player1.deal_hand(self.deck) 
        self.player2.deal_hand(self.deck)
        for card in self.player1.cards_in_hand:
            self.game_screen.display_cards(self.player1.cards_in_hand)
        for card in self.player2.cards_in_hand:
            self.game_screen.display_cards(self.player2.cards_in_hand, False)
            
        
    def is_game_over(self, discard_area):
        if len(discard_area.cards) >= 10:
            return True
        return False

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck)  
        
        
        while not self.is_game_over():
            self.player1.take_turn(self.deck, self.discard_area)
            if self.is_game_over():  
                break

            self.player2.take_turn(self.deck, self.discard_area)
            if self.is_game_over():  
                break
        
        
        for card in self.player1.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player1.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
                
        for card in self.player2.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player2.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
        
                
        
        player1_score = self.player1.calculate_total_points(self.player1.cards_in_hand) 
        player2_score = self.player2.calculate_total_points(self.player2.cards_in_hand)
        print(f"Player 1 Score: {player1_score}") 
        print(f"Player 2 Score: {player2_score}") 
    
    """def draw_card_to_hand(self):
        card = self.deck.draw_card()
        self.player"""
        #draw a card
        #select a card to discard
        #table list append card that's discarded
        #player 2 turn
        #draw a card or take one from table
        #analyze cards on a table and if value added is >= 25 takes that card from table
        #remove worst card    
            
        

    