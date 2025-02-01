from card import *


class Blizzard(Card):
  def __init__(self):
    super().__init__("Blizzard", 30, WEATHER, 12)
    self.penalty = True    

  @Card.not_blank
  def condition(self, hand):  
    if self.penalty:
      for card in hand:
        if card.suit == FLOOD:
          card.blank()
          
    count = sum(1 for card in hand if card.suit in {ARMY, LEADER, BEAST, FLAME})
    self.total_power += count * -5