from card import *

class DwarvishInfantry(Card):
    def __init__(self):
        super().__init__("Dwarvish Infantry", 15, ARMY, 24)
        self.has_penalty = True
        self.penalties_suits = {ARMY}
        self.image = "images/dwarvish_infantry.jpeg"
        self.save_original_state()  
        


    @Card.not_blank
    def penalty(self, hand):
        if self.has_penalty:             
            count_army = sum(1 for card in hand if card.suit in self.penalties_suits and card is not self) 
            self.total_power += count_army * -2