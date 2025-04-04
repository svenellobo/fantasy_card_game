from card import *

class Candle(Card):
    def __init__(self):
        super().__init__("Candle", 2, FLAME, 17)
        self.image = "images/candle.jpeg"
        self.save_original_state()    
        

    @Card.not_blank
    def bonus(self, hand):    
        bonus = {card.name for card in hand}
        if {"Book of Changes", "Bell Tower"}.issubset(bonus) and any(card.suit == WIZARD for card in hand):
            self.total_power += 100