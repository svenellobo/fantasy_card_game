from deck import Deck
from hand import Hand

class Game():
    def __init__(self):
        self.deck = Deck()
        self.player1 = Hand()
        self.player2 = Hand()

    def play(self):
        self.deal_hand(self.player1.cards_in_hand)
        self.deal_hand(self.player2.cards_in_hand)

        # SET HAND VALUE FOR CARDS IN HAND
        # for cards in self.player1.cards_in_hand: cards.hand = self.player1.cards_in_hand

    def deal_hand(self, hand):
        for i in range(7):
            card = self.deck.deal_card()
            hand.append(card)