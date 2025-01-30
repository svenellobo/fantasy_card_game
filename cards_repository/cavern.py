from card import Card


class Cavern(Card):
  def __init__(self):
    super().__init__("Cavern", 6, "Land", 2)
    self.condition()


  def condition(self, hand):
    for card in hand:
      if card.name == "Dwarvish Infantry" or card.name == "Dragon":
        self.power += 25
    
      if card.suit == "Weather":
          card.penalty = None