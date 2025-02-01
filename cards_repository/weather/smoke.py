from card import *


class Smoke(Card):
  def __init__(self):
    super().__init__("Smoke", 27, WEATHER, 13)
    self.penalty = True    

  @Card.not_blank
  def condition(self, hand):  
    if self.penalty:
      if not any(card.suit == FLAME for card in hand):
        self.blank()