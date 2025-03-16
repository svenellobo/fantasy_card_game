from card import *


class Smoke(Card):
    def __init__(self):
        super().__init__("Smoke", 27, WEATHER, 13)
        self.has_penalty = True
        self.penalties_suits = {FLAME} 
        self.save_original_state()   

    @Card.not_blank
    def condition(self, hand):  
        if self.has_penalty:
            if not any(card.suit in self.penalties_suits for card in hand):
                self.blank()