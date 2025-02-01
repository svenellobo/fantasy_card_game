from card import *

class Rangers(Card):
  def __init__(self):
    super().__init__("Rangers", 5, ARMY, 25)   
    self.has_clear = True


  @Card.not_blank
  def condition(self, hand):    
    count_lands = sum(1 for card in hand if card.suit)
    self.total_power += count_lands * 10

  def clear(self, hand):
    for card in hand:
      if card.name != "War Dirigible" and card.has_penalty == True:
        





