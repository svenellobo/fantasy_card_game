from deck import Deck
from hand import Hand
from cpu_player import CPUPlayer

class Game():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = Hand()
        self.player2 = CPUPlayer()

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck)        
        
            
        for card in self.player1.cards_in_hand:
            card.clear_penalties(self.player1.cards_in_hand)
            
        for card in self.player1.cards_in_hand:
            card.condition(self.player1.cards_in_hand)
        
            
            
        for card in self.players[0].hand:
            card.clear_penalties(self.player1.hand)
        # SET HAND VALUE FOR CARDS IN HAND
        # for cards in self.player1.cards_in_hand: cards.hand = self.player1.cards_in_hand

    