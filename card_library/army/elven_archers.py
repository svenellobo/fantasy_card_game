from card import *

class ElvenArchers(Card):
    def __init__(self):
        super().__init__("Elven Archers", 10, ARMY, 22)
        self.save_original_state()
        
       
        


    @Card.not_blank
    def condition(self, hand):    
        if not any(card.suit == WEATHER for card in hand):
            self.total_power += 5