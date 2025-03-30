from card import *

class Warship(Card):
    def __init__(self):
        super().__init__("Warship", 23, WEAPON, 41)
        self.has_penalty = True
        self.has_clear = True
        self.has_blank = True
        self.blanks_self=True 
        self.penalties_suits = {FLOOD}
        self.save_original_state()
        
        
    @Card.not_blank
    def activate_blank(self,hand):
        if self.has_penalty:                        
            if not any(card.suit in self.penalties_suits for card in hand):
                self.blank()
                
    def clear_penalties(self, hand):       
        for card in hand:
            if card.suit == FLOOD:                
                card.penalties_suits.discard(ARMY)