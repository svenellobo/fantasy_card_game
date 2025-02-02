from card import *


class Warlord(Card):
    def __init__(self):
        super().__init__("Warlord", 4, LEADER, 34)   

    @Card.not_blank
    def condition(self, hand): 
        self.total_power += sum(card.base_power for card in hand if card.suit == ARMY)   
    