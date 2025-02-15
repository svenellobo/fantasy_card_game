from card import *


class Queen(Card):
    def __init__(self):
        super().__init__("Queen", 6, LEADER, 32)   

    @Card.not_blank
    def condition(self, hand):    
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
      
