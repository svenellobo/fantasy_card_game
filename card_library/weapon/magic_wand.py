from card import *

class MagicWand(Card):
    def __init__(self):
        super().__init__("Magic Wand", 1, WEAPON, 42)
        self.save_original_state()
        
        
    @Card.not_blank   
    def bonus(self, hand):
        if any(card.suit == WIZARD for card in hand):
            self.total_power += 25