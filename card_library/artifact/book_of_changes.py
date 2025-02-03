from card import *

class BookOfChanges(Card):
    def __init__(self):
        super().__init__("Book of Changes", 3, ARTIFACT, 49)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        pass