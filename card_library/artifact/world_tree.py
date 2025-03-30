from card import *

class WorldTree(Card):
    def __init__(self):
        super().__init__("World Tree", 2, ARTIFACT, 48)
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def bonus(self, hand):
        card_count = 0
        set_of_suits = set()   
        for card in hand:
            if card.suit != None:
                set_of_suits.add(card.suit)
                card_count += 1
        if len(set_of_suits) == card_count:
            self.total_power += 50