from card import *

class Forge(Card):
    def __init__(self):
        super().__init__("Forge", 9, FLAME, 18)    
        

    @Card.not_blank
    def condition(self, hand):    
        count = sum(1 for card in hand if card.suit == ARTIFACT or card.suit == WEAPON)
        self.total_power += count * 9