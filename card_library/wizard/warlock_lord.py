from card import *

class WarlockLord(Card):
    def __init__(self):
        super().__init__("Warlock Lord", 25, WIZARD, 29)
        self.has_penalty = True
        self.penalties_suits = {LEADER, WIZARD}
        self.image = resource_path("images/warlock_lord.jpeg")
        self.save_original_state()   
        


    @Card.not_blank
    def penalty(self, hand):    
        if self.has_penalty:
            count = sum(1 for card in hand if card.suit in self.penalties_suits) -1
            self.total_power += count * -10