from card import *

class Candle(Card):
    def __init__(self):
        super().__init__("Candle", 2, FLAME, 17)    
        

    @Card.not_blank
    def condition(self, hand):    
        bonus = {card.name for card in hand}
        if {"Book of Changes", "Bell Tower"}.issubset(bonus) and any(card.suit == WIZARD for card in hand):
            self.total_power += 100