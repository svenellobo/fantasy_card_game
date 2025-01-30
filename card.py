class Card():
  def __init__(self, name, base_power, suit):
    self.name = name
    self.base_power = base_power
    self.suit = suit

  def __str__(self):
    return f"Card {self.name} belongs to {self.suit} suit and has base power of {self.base_power}"