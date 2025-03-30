from card import *

class Mirage(Card):
    def __init__(self):
        super().__init__("Mirage", 0, WILD, 52)
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def effect(self, hand):        
        
        pass