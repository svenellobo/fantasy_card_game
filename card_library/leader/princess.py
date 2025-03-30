from card import *


class Princess(Card):
    def __init__(self):
        super().__init__("Princess", 2, LEADER, 33) 
        self.save_original_state()  

    @Card.not_blank
    def bonus(self, hand):        
        count = sum(1 for card in hand if card.suit in {ARMY, WIZARD} or ((card.suit == LEADER) and (card is not self)))
        self.total_power += count * 8