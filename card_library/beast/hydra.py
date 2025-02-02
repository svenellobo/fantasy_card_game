from card import *

class Hydra(Card):
    def __init__(self):
        super().__init__("Hydra", 12, BEAST, 40)
        
        
    @Card.not_blank   
    def condition(self, hand):
        if any(card.name == "Swamp" for card in hand):
            self.total_power += 28