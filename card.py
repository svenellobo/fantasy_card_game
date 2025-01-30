class Card():
  def __init__(self, name, power, suit, card_nmb):
    self.name = name
    self.power = power
    self.suit = suit
    self.card_nmb = card_nmb
    self.hand = None
    self.penalty = None

  def __str__(self):
    return f"Card {self.card_nmb} {self.name} belongs to {self.suit} suit and has base power of {self.power}"
  
  
  def condition(self):
    pass

