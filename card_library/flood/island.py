from card import *

class Island(Card):
    def __init__(self):
        super().__init__("Island", 14, FLOOD, 9)
        self.has_clear = True        
        self.image = "images/island.jpeg"
        self.save_original_state()   

        
    def clear_penalties(self, hand):
        filtered_hand = [card for card in hand if card.suit in {FLOOD, FLAME}]
        if filtered_hand:
            max_power_card = max(filtered_hand, key=lambda card: card.base_power)
            max_power_card.has_penalty = False
