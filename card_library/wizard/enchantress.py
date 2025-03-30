from card import *

class Enchantress(Card):
    def __init__(self):
        super().__init__("Enchantress", 5, WIZARD, 30) 
        self.save_original_state()     
        


    @Card.not_blank
    def bonus(self, hand):    
        count = sum(1 for card in hand if card.suit in {LAND, WEATHER, FLOOD, FLAME})
        self.total_power += count * 5