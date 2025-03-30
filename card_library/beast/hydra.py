from card import *

class Hydra(Card):
    def __init__(self):
        super().__init__("Hydra", 12, BEAST, 40)
        self.save_original_state()
        
        
    @Card.not_blank   
    def bonus(self, hand):
        if any(card.name == "Swamp" for card in hand):
            self.total_power += 28