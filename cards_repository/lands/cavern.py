from card import Card


class Cavern(Card):
  def __init__(self):
    super().__init__("Cavern", 6, "Land", 2)
    


  def condition(self, hand):
    if any(card.name in {"Dwarvish Infantry", "Dragon"} for card in hand):
      self.total_power += 25
                
    for card in hand:
      if card.suit == "Weather":
          card.penalty = False