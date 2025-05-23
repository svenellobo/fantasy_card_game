from card import *


class BellTower(Card):
  def __init__(self):
    super().__init__("Bell Tower", 8, LAND, 3)
    self.image = resource_path("images/bell_tower.jpeg")
    self.save_original_state()   

  @Card.not_blank
  def bonus(self, hand):
    if any(card.suit == WIZARD for card in hand):
        self.total_power += 15
    