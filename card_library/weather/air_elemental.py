from card import *


class AirElemental(Card):
    def __init__(self):
        super().__init__("Air Elemental", 4, WEATHER, 15)
        self.image = resource_path("images/air_elemental.jpeg")
        self.save_original_state()
        

    @Card.not_blank
    def bonus(self, hand):  
        weather_count = sum(1 for card in hand if card.suit == WEATHER and card is not self)              
        self.total_power += weather_count * 15
        