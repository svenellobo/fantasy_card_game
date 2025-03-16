from card import *

class WorldTree(Card):
    def __init__(self):
        super().__init__("World Tree", 2, ARTIFACT, 48)
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        set_of_suits = set()
        set_of_names = set()
        len_of_suits = len({item for item in set_of_suits if item is not None})
        len_of_names = len({item for item in set_of_suits if item is not None})
        for card in hand:
            set_of_suits.add(card.suit)
            set_of_names.add(card.name)
        if len_of_suits == len_of_names:
            self.total_power += 50