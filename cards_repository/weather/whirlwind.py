from card import *


class Whirlwind(Card):
  def __init__(self):
    super().__init__("Whirlwind", 13, WEATHER, 14)
        

  @Card.not_blank
  def condition(self, hand):  
    if any(card.name == "Rainstorm" for card in hand) and any(card.name in {"Blizzard", "Great Flood"} for card in hand):
      self.total_power += 40