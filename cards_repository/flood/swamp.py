from card import *

class Swamp(Card):
  def __init__(self):
    super().__init__("Swamp", 18, FLOOD, 7)
    self.penalty = True
    

  @Card.not_blank
  def condition(self, hand):
    if self.penalty:
      count = sum(1 for card in hand if card.suit in {ARMY, FLAME})
      self.total_power -= count * 3