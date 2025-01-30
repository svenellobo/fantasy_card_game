from card import Card


class Mountain(Card):
  def __init__(self):
    super().__init__("Mountain", 9, "Land", 1)
    self.condition()


  def condition(self, hand):
    card_names = {card.name for card in hand}
    if {"Smoke", "Wildfire"}.issubset(card_names):
      self.power += 50
    for card in hand:
      if card.suit == "Floods":
          card.penalty = None
    
