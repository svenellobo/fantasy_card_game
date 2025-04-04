from card import *

class Unicorn(Card):
    def __init__(self):
        super().__init__("Unicorn", 9, BEAST, 36)
        self.image = "images/unicorn.jpeg"
        self.save_original_state()
        
        
    @Card.not_blank   
    def bonus(self, hand):
        if any(card.name == "Princess" for card in hand):
            self.total_power += 30
        elif any(card.name in ("Empress", "Queen", "Enchantress") for card in hand):
            self.total_power += 15
        
        
        
        
            