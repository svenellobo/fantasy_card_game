from card import *

class ProtectionRune(Card):
    def __init__(self):
        super().__init__("Protection Rune", 1, ARTIFACT, 50)
        self.has_clear = True
        self.image = resource_path("images/protection_rune.jpeg")
        self.save_original_state()
        
        
        
    def clear_penalties(self, hand):              
        for card in hand:
            card.has_penalty = False