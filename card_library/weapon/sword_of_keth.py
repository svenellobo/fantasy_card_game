from card import *

class SwordOfKeth(Card):
    def __init__(self):
        super().__init__("Sword of Keth", 7, WEAPON, 43)
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        if any(card.suit == LEADER for card in hand) and any(card.name == "Shield of Keth" for card in hand):
            self.total_power += 40
        elif any(card.suit == LEADER for card in hand):
            self.total_power += 10
        