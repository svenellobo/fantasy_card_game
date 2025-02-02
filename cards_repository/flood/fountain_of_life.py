from card import *

class FountainOfLife(Card):
    def __init__(self):
        super().__init__("Fountain of Life", 1, FLOOD, 6)


    @Card.not_blank
    def condition(self, hand):
        max_power = max(card.base_power for card in hand if card.suit in {WEAPON, FLOOD, FLAME, LAND, WEATHER})
        self.total_power += max_power
    