from card import *

class Wildfire(Card):
    def __init__(self):
        super().__init__("Wildfire", 40, FLAME, 16)
        self.has_penalty = True
        self.penalties_names = {"Mountain", "Great Flood", "Island", "Unicorn", "Dragon"}
        self.penalties_suits = {FLAME, WIZARD, WEATHER, WEAPON, }
        

    @Card.not_blank
    def condition(self, hand):    
        if self.has_penalty:
            for card in hand:        
                if card.suit not in self.penalties_suits and card.name not in self.penalties_names:
                    card.blank()