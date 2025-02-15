from card import *

class ShieldOfKeth(Card):
    def __init__(self):
        super().__init__("Shield of Keth", 4, ARTIFACT, 46)
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        if any(card.suit == LEADER for card in hand) and any(card.name == "Sword of Keth" for card in hand):
            self.total_power += 40
        elif any(card.suit == LEADER for card in hand):
            self.total_power += 15