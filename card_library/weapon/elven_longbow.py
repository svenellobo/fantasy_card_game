from card import *

class ElvenLongbow(Card):
    def __init__(self):
        super().__init__("Elven Longbow", 3, WEAPON, 44)
        self.image = "images/elven_longbow.jpeg"
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def bonus(self, hand):        
        if any(card.name in ("Elven Archers", "Warlord", "Beastmaster") for card in hand):
            self.total_power += 30
        