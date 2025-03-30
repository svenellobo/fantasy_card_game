from card import *

class Beastmaster(Card):
    def __init__(self):
        super().__init__("Beastmaster", 9, WIZARD, 27)      
        self.has_clear = True
        self.save_original_state()


    @Card.not_blank
    def bonus(self, hand):    
        count_beasts = sum(1 for card in hand if card.suit == BEAST)     
        self.total_power += count_beasts * 9
            
    def clear_penalties(self, hand):
        for card in hand:
            if card.suit == BEAST:
                    card.has_penalty = False


      
        