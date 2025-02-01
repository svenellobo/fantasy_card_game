from card import *


class Rainstorm(Card):
  def __init__(self):
    super().__init__("Rainstorm", 8, WEATHER, 11)
    self.penalty = True    

  @Card.not_blank
  def condition(self, hand):
    flood_count = sum(1 for card in hand if card.suit == FLOOD) 
    self.total_power += flood_count * 10

    if self.penalty:
      for card in hand:
        if card.name != "Lightning" and card.suit == FLAME:
          card.blank()