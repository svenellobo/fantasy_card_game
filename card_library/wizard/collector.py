from card import *

class Collector(Card):
    def __init__(self):
        super().__init__("Collector", 7, WIZARD, 26)
        self.image = "images/collector.jpeg"
        self.save_original_state()      
        


    @Card.not_blank
    def bonus(self, hand):    
        suits_dict = {}
        
        for card in hand:
            if card.suit not in suits_dict:
                suits_dict[card.suit] = set()
            suits_dict[card.suit].add(card.name)  
        
        for suit, names in suits_dict.items():
            suit_count = len(names)  

            if suit_count == 3:
                self.total_power += 10
            elif suit_count == 4:
                self.total_power += 40
            elif suit_count == 5:
                self.total_power += 100