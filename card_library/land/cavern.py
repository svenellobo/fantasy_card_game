from card import *


class Cavern(Card):
    def __init__(self):
        super().__init__("Cavern", 6, LAND, 2)
        self.has_clear = True
        self.image = resource_path("images/cavern.jpeg")
        self.save_original_state()

    @Card.not_blank
    def bonus(self, hand):
        if any(card.name in {"Dwarvish Infantry", "Dragon"} for card in hand):
            self.total_power += 25
                        
    def clear_penalties(self, hand):               
        for card in hand:
            if card.suit == WEATHER:
                card.has_penalty = False