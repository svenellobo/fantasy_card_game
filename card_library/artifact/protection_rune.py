from card import *

class ProtectionRune(Card):
    def __init__(self):
        super().__init__("Protection Rune", 1, ARTIFACT, 50)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        for card in hand:
            card.has_penalty = False