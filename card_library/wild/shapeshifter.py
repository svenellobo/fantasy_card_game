from card import *

class Shapeshifter(Card):
    def __init__(self):
        super().__init__("Shapeshifter", 0, WILD, 51)
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def effect(self, hand):        
        
        pass