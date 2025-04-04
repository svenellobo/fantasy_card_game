from card import *


class Rainstorm(Card):
    def __init__(self):
        super().__init__("Rainstorm", 8, WEATHER, 11)
        self.has_penalty = True
        self.has_blank = True        
        self.penalties_suits = {FLAME}    
        self.penalties_names = {"Lightning"}
        self.image = "images/rainstorm.jpeg"
        self.save_original_state()

    @Card.not_blank
    def bonus(self, hand):
        flood_count = sum(1 for card in hand if card.suit == FLOOD) 
        self.total_power += flood_count * 10
        
    @Card.not_blank
    def activate_blank(self,hand):
        if self.has_penalty:
            for card in hand:
                if card.suit in self.penalties_suits and card.name not in self.penalties_names:
                    card.blank()  