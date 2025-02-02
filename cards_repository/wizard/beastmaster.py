from card import *

class Beastmaster(Card):
    def __init__(self):
        super().__init__("Beastmaster", 9, WIZARD, 27)      
        self.has_clear = True


    @Card.not_blank
    def condition(self, hand):    
        count_beasts = 0
        
        for card in hand:
            if card.suit == BEAST:
                count_beasts += 1
                if card.has_penalty:
                    card.has_penalty = False
        self.total_power += count_beasts * 9


      
        