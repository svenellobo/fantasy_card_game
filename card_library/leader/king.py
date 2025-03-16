from card import *


class King(Card):
    def __init__(self):
        super().__init__("King", 8, LEADER, 31)
        self.save_original_state()   

    @Card.not_blank
    def condition(self, hand):    
        count_army = 0
        has_queen = False
        for card in hand:
            if card.suit == ARMY:
                count_army += 1
            if card.name == "Queen":
                has_queen = True


        if has_queen:
            self.total_power += count_army * 20

        else:
            self.total_power += count_army * 5
      