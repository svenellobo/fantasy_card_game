from card import *


class Empress(Card):
    def __init__(self):
        super().__init__("Empress", 15, LEADER, 35)
        self.has_penalty = True
        self.penalties_suits = {LEADER}
        self.save_original_state()

    @Card.not_blank
    def condition(self, hand):
        army_count = 0
        leader_count = -1
        for card in hand:
            if self.has_penalty:
                if card.suit in self.penalties_suits:
                    leader_count += 1
            if card.suit == ARMY:                
                army_count += 1
            
        self.total_power += (army_count * 10) + (leader_count * -5)
             
           
           
           

            
