from card import *


class Blizzard(Card):
    def __init__(self):
        super().__init__("Blizzard", 30, WEATHER, 12)
        self.has_penalty = True
        self.has_blank = True
        self.penalties_suits = {ARMY, LEADER, BEAST, FLAME}
        self.image = "images/blizzard.jpeg"
        self.save_original_state()    

    @Card.not_blank
    def penalty(self, hand):
        if self.has_penalty:                  
            count = sum(1 for card in hand if card.suit in self.penalties_suits)
            self.total_power += count * -5
            
    @Card.not_blank
    def activate_blank(self,hand): 
        if self.has_penalty:
            for card in hand:
                if card.suit == FLOOD:
                    card.blank()