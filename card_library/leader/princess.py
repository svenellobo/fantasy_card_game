from card import *


class Princess(Card):
    def __init__(self):
        super().__init__("Princess", 2, LEADER, 33)   

    @Card.not_blank
    def condition(self, hand):    
        count = sum(1 for card in hand if card.suit in {ARMY, WIZARD, LEADER}) -1
        self.total_power += count * 8