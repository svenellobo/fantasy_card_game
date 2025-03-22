from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea

class Game():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = CPUPlayer()
        self.player2 = CPUPlayer()
        self.discard_area = DiscardArea()
        
    
        
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
                card.condition(self.player1.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
                
        for card in self.player2.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.condition(self.player2.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
        
                
        
        player1_score = self.player1.calculate_total_points(self.player1.cards_in_hand) 
        player2_score = self.player2.calculate_total_points(self.player2.cards_in_hand)
        print(f"Player 1 Score: {player1_score}") 
        print(f"Player 2 Score: {player2_score}") 
    
        
        #draw a card
        #select a card to discard
        #table list append card that's discarded
        #player 2 turn
        #draw a card or take one from table
        #analyze cards on a table and if value added is >= 25 takes that card from table
        #remove worst card    
            
        

    