from card import *


class Smoke(Card):
    def __init__(self):
        super().__init__("Smoke", 27, WEATHER, 13)
        self.has_penalty = True
        self.has_blank = True
        self.blanks_self=True
        self.penalties_suits = {FLAME} 
        self.save_original_state()
           

    @Card.not_blank
    def activate_blank(self,hand):   
        if self.has_penalty:            
            if not any(card.suit in self.penalties_suits for card in hand):
                self.blank()