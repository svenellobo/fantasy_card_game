from card import *

class Unicorn(Card):
    def __init__(self):
        super().__init__("Unicorn", 9, BEAST, 36)
        
        
    @Card.not_blank   
    def condition(self, hand):
        if any(card.name in ("Empress", "Queen", "Enchantress") for card in hand):
            self.total_power += 15
        elif any(card.name == "Princess" for card in hand):
            self.total_power += 30
        
        
        
            