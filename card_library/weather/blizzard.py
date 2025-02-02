from card import *


class Blizzard(Card):
    def __init__(self):
        super().__init__("Blizzard", 30, WEATHER, 12)
        self.has_penalty = True
        self.penalties_suits = {ARMY, LEADER, BEAST, FLAME}    

    @Card.not_blank
    def condition(self, hand):  
        if self.has_penalty:
            for card in hand:
                if card.suit == FLOOD:
                    card.blank()
            
        count = sum(1 for card in hand if card.suit in self.penalties_suits)
        self.total_power += count * -5