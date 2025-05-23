from card import *

class Rangers(Card):
    def __init__(self):
        super().__init__("Rangers", 5, ARMY, 25)   
        self.has_clear = True
        self.image = resource_path("images/rangers.jpeg")
        self.save_original_state()


    @Card.not_blank
    def bonus(self, hand):    
        count_lands = sum(1 for card in hand if card.suit == LAND)
        self.total_power += count_lands * 10
        
    def clear_penalties(self, hand):        
        for card in hand:
            if card.name != "War Dirigible":
                card.penalties_suits.discard(ARMY)





