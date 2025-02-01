from card import *


class EarthElemental(Card):
  def __init__(self):
    super().__init__("Earth Elemental", 4, LAND, 5)    

  @Card.not_blank
  def condition(self, hand):
    land_count = sum(1 for card in hand if card.suit == LAND) - 1
    self.total_power += land_count * 15
    
    