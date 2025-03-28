from card import *

class FireElemental(Card):
    def __init__(self):
        super().__init__("Fire Elemental", 4, FLAME, 20)
        self.save_original_state()    
        

    @Card.not_blank
    def condition(self, hand):   
        flame_count = sum(1 for card in hand if card.suit == FLAME and card is not self)
        self.total_power += flame_count * 15