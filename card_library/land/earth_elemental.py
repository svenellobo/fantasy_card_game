from card import *


class EarthElemental(Card):
    def __init__(self):
        super().__init__("Earth Elemental", 4, LAND, 5)
        self.image = "images/earth_elemental.jpeg" 
        self.save_original_state()   

    @Card.not_blank
    def bonus(self, hand):
        land_count = sum(1 for card in hand if card.suit == LAND and card is not self)
        self.total_power += land_count * 15
    
    