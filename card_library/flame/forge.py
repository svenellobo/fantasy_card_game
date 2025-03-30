from card import *

class Forge(Card):
    def __init__(self):
        super().__init__("Forge", 9, FLAME, 18) 
        self.save_original_state()   
        

    @Card.not_blank
    def bonus(self, hand):    
        count = sum(1 for card in hand if card.suit == ARTIFACT or card.suit == WEAPON)
        self.total_power += count * 9