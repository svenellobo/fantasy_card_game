from card import *

class Shapeshifter(Card):
    def __init__(self):
        super().__init__("Shapeshifter", 0, WILD, 51)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        
        pass