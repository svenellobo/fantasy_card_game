from card import *


class Mountain(Card):
    def __init__(self):
        super().__init__("Mountain", 9, LAND, 1)
        self.has_clear = True
        self.image = resource_path("images/mountain.jpeg")
        self.save_original_state()

    @Card.not_blank
    def bonus(self, hand):
        card_names = {card.name for card in hand}
        if {"Smoke", "Wildfire"}.issubset(card_names):
            self.total_power += 50     
    
    def clear_penalties(self, hand):
        for card in hand:
            if card.suit == FLOOD:
                card.has_penalty = False