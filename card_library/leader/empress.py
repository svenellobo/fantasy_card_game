from card import *


class Empress(Card):
    def __init__(self):
        super().__init__("Empress", 15, LEADER, 35)
        self.has_penalty = True
        self.penalties_suits = {LEADER}
        self.save_original_state()

    @Card.not_blank
    def condition(self, hand):
        army_count = sum(1 for card in hand if card.suit == ARMY)
        leader_count = 0
        if self.has_penalty:
            leader_count = sum(1 for card in hand if card.suit in self.penalties_suits and card is not self)       
            
        self.total_power += (army_count * 10) + (leader_count * -5)
             
           
           
           

            
