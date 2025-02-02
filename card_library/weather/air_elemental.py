from card import *


class AirElemental(Card):
    def __init__(self):
        super().__init__("Air Elemental", 4, WEATHER, 15)
        

    @Card.not_blank
    def condition(self, hand):  
        weather_count = sum(1 for card in hand if card.suit == WEATHER) - 1
        self.total_power += weather_count * 15