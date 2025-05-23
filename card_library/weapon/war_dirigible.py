from card import *

class WarDirigible(Card):
    def __init__(self):
        super().__init__("War Dirigible", 35, WEAPON, 45)
        self.has_penalty = True               
        self.has_blank = True
        self.blanks_self=True 
        self.penalties_suits = {ARMY, WEATHER}
        self.image = resource_path("images/war_dirigible.jpeg")
        self.save_original_state()       
       
    
                
    @Card.not_blank
    def activate_blank(self,hand):       
        if self.has_penalty:                
            if not any(card.suit == ARMY for card in hand):
                self.blank()
            if any(card.suit == WEATHER for card in hand):
                self.blank()
                