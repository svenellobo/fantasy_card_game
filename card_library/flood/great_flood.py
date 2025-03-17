from card import *

class GreatFlood(Card):
    def __init__(self):
        super().__init__("Great Flood", 32, FLOOD, 8)
        self.has_penalty = True
        self.has_blank = True
        self.penalties_suits = {ARMY, LAND, FLAME}
        self.penalties_names = {"Mountain", "Lightning"}
        self.save_original_state()
        

    @Card.not_blank
    def activate_blank(self,hand):
        if self.has_penalty:
            for card in hand:          
                if card.suit in self.penalties_suits and card.name not in self.penalties_names:
                    card.blank()

  