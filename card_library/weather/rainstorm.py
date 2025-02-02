from card import *


class Rainstorm(Card):
    def __init__(self):
        super().__init__("Rainstorm", 8, WEATHER, 11)
        self.has_penalty = True
        self.penalties_suits = {FLAME}    
        self.penalties_names = {"Lightning"}

    @Card.not_blank
    def condition(self, hand):
        flood_count = sum(1 for card in hand if card.suit == FLOOD) 
        self.total_power += flood_count * 10

        if self.has_penalty:
            for card in hand:
                if card.name not in self.penalties_names and card.suit in self.penalties_suits:
                    card.blank()  