from card import *

class Lightning(Card):
    def __init__(self):
        super().__init__("Lightning", 11, FLAME, 19)
        self.save_original_state()    
        

    @Card.not_blank
    def bonus(self, hand):    
        if any(card.name == "Rainstorm" for card in hand):
            self.total_power += 30