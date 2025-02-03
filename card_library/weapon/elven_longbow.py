from card import *

class ElvenLongbow(Card):
    def __init__(self):
        super().__init__("Elven Longbow", 3, WEAPON, 44)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        if any(card.name in ("Elven Archers", "Warlord", "Beastmaster") for card in hand):
            self.total_power += 30
        