from card import *

class Mirage(Card):
    def __init__(self):
        super().__init__("Mirage", 0, WILD, 52)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        
        pass