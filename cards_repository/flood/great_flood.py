from card import *

class GreatFlood(Card):
  def __init__(self):
    super().__init__("Great Flood", 32, FLOOD, 8)
    self.penalty = True
    

  @Card.not_blank
  def condition(self, hand):
    if self.penalty:
      for card in hand:
        if card.suit == ARMY or (card.suit == LAND and card.name != "Mountain") or (card.suit == FLAME and card.name != "Lightning"):
          card.blank()

  