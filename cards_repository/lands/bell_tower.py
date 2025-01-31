from card import Card


class BellTower(Card):
  def __init__(self):
    super().__init__("Bell Tower", 8, "Land", 3)    


  def condition(self, hand):
    if any(card.suit == "Wizard" for card in hand):
      self.total_power += 15
    