from card import *

class ShieldOfKeth(Card):
    def __init__(self):
        super().__init__("Shield of Keth", 4, ARTIFACT, 46)
        self.image = "images/shield_of_keth.jpeg"
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def bonus(self, hand):        
        if any(card.suit == LEADER for card in hand) and any(card.name == "Sword of Keth" for card in hand):
            self.total_power += 40
        elif any(card.suit == LEADER for card in hand):
            self.total_power += 15