from card import *

class FireElemental(Card):
    def __init__(self):
        super().__init__("Fire Elemental", 4, FLAME, 20)    
        

    @Card.not_blank
    def condition(self, hand):    
        flame_count = sum(1 for card in hand if card.suit == FLAME) - 1
        self.total_power += flame_count * 15