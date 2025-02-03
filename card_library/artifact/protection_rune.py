from card import *

class ProtectionRune(Card):
    def __init__(self):
        super().__init__("Protection Rune", 1, ARTIFACT, 50)
        
        
        
    def clear_penalties(self, hand):              
        for card in hand:
            card.has_penalty = False