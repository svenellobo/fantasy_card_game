from card import *

class LightCavalry(Card):
    def __init__(self):
        super().__init__("Light Cavalry", 17, ARMY, 23)
        self.has_penalty = True
        self.penalties_suits = {LAND} 
        self.image = resource_path("images/light_cavalry.jpeg")
        self.save_original_state()        


    @Card.not_blank
    def penalty(self, hand):
        if self.has_penalty:    
            count_lands = sum(1 for card in hand if card.suit in self.penalties_suits)
            self.total_power += count_lands * -2