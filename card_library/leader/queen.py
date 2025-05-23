from card import *


class Queen(Card):
    def __init__(self):
        super().__init__("Queen", 6, LEADER, 32) 
        self.image = resource_path("images/queen.jpeg")
        self.save_original_state()  

    @Card.not_blank
    def bonus(self, hand):    
        count_army = 0
        has_king = False
        for card in hand:
            if card.suit == ARMY:
                count_army += 1
            if card.name == "King":
                has_king = True

        if has_king:
            self.total_power += count_army * 20
        else:
            self.total_power += count_army * 5
      
