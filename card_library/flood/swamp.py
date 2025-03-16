from card import *

class Swamp(Card):
    def __init__(self):
        super().__init__("Swamp", 18, FLOOD, 7)
        self.has_penalty = True
        self.penalties_suits = {ARMY, FLAME}
        self.save_original_state()
        

    @Card.not_blank
    def condition(self, hand):
        if self.has_penalty:
            count = sum(1 for card in hand if card.suit in self.penalties_suits)
            self.total_power -= count * 3