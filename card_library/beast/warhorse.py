from card import *

class Warhorse(Card):
    def __init__(self):
        super().__init__("Warhorse", 6, BEAST, 38)
        self.image = "images/warhorse.jpeg"
        self.save_original_state()
        
        
    @Card.not_blank   
    def bonus(self, hand):
        if any(card.suit in (LEADER, WIZARD) for card in hand):
            self.total_power += 14