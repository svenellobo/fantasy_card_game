from card import *


class Forest(Card):
    def __init__(self):
        super().__init__("Forest", 7, LAND, 4)
        self.image = resource_path("images/forest.jpeg")
        self.save_original_state()
        

    @Card.not_blank
    def bonus(self, hand):
        for card in hand:
            if card.suit == BEAST or card.name == "Elven Archers":
                self.total_power += 12
      
      

    