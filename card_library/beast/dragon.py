from card import *

class Dragon(Card):
    def __init__(self):
        super().__init__("Dragon", 30, BEAST, 39)
        self.has_penalty = True
        self.penalties_suits = {WIZARD}
        self.save_original_state()
        
    @Card.not_blank   
    def penalty(self, hand):
        if self.has_penalty:
            if not any(card.suit in self.penalties_suits for card in hand):
                self.total_power -= 40