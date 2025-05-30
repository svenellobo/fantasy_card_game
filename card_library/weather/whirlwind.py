from card import *


class Whirlwind(Card):
    def __init__(self):
        super().__init__("Whirlwind", 13, WEATHER, 14)
        self.image = resource_path("images/whirlwind.jpeg")
        self.save_original_state()
            

    @Card.not_blank
    def bonus(self, hand):  
        if any(card.name == "Rainstorm" for card in hand) and any(card.name in {"Blizzard", "Great Flood"} for card in hand):
            self.total_power += 40