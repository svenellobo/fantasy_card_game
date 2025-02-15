from card import *

class GreatFlood(Card):
    def __init__(self):
        super().__init__("Great Flood", 32, FLOOD, 8)
        self.has_penalty = True
        self.penalties_suits = {ARMY, LAND, FLAME}
        self.penalties_names = {"Mountain", "Lightning"}
        

    @Card.not_blank
    def condition(self, hand):
        if self.has_penalty:
            for card in hand:          
                if card.suit in self.penalties_suits and card.name not in self.penalties_names:
                    card.blank()

  