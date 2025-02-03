from card import *

class Doppelganger(Card):
    def __init__(self):
        super().__init__("Doppelganger", 0, WILD, 53)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        highest_power = max(card.base_power for card in hand)
        pass
        
        
    
        