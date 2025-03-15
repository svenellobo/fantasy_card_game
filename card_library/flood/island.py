from card import *

class Island(Card):
    def __init__(self):
        super().__init__("Island", 14, FLOOD, 9)
        self.has_clear = True    

        
    def clear_penalties(self, hand):
        filtered_hand = [card for card in hand if card.suit in {FLOOD, FLAME}]
        max_power_card = max(filtered_hand, key=lambda card: card.base_power)
        max_power_card.penalty = False
