from card import *

class Knights(Card):
    def __init__(self):
        super().__init__("Knights", 20, ARMY, 21)
        self.has_penalty = True
        self.penalties_suits = {LEADER}
        self.image = "images/dwarvish_infantry.jpeg" 
        self.save_original_state()  
        


    @Card.not_blank
    def penalty(self, hand):
        if self.has_penalty:    
            if not any(card.suit in self.penalties_suits for card in hand):
                self.total_power -= 8