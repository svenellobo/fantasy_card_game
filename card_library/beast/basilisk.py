from card import *

class Basilisk(Card):
    def __init__(self):
        super().__init__("Basilisk", 35, BEAST, 37)
        self.has_penalty = True
        self.has_blank = True
        self.penalties_suits = {ARMY}
        self.save_original_state()
        
        
        
    @Card.not_blank
    def activate_blank(self,hand):
        if self.has_penalty:
            for card in hand:                
                if card.suit == LEADER or card.suit in self.penalties_suits or (card.suit == BEAST and card is not self):
                    card.blank()
        
    