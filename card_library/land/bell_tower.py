from card import *


class BellTower(Card):
  def __init__(self):
    super().__init__("Bell Tower", 8, LAND, 3)    

  @Card.not_blank
  def condition(self, hand):
    if any(card.suit == WIZARD for card in hand):
        self.total_power += 15
    