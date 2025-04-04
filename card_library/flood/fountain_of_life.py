from card import *

class FountainOfLife(Card):
    def __init__(self):
        super().__init__("Fountain of Life", 1, FLOOD, 6)
        self.image = "images/fountain_of_life.jpeg"
        self.save_original_state()


    @Card.not_blank
    def bonus(self, hand):
        filtered_hand = [card for card in hand if card.suit in {WEAPON, FLOOD, FLAME, LAND, WEATHER}]
        if filtered_hand:
            max_power_card = max(filtered_hand, key=lambda card: card.base_power)
            self.total_power += max_power_card.base_power
        
    