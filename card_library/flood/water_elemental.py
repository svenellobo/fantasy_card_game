from card import *


class WaterElemental(Card):
    def __init__(self):
        super().__init__("Water Elemental", 4, FLOOD, 10) 
        self.save_original_state()   

    @Card.not_blank
    def condition(self, hand):
        flood_count = sum(1 for card in hand if card.suit == FLOOD and card is not self)
        self.total_power += flood_count * 15