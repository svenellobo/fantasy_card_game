from card import Card


class Forest(Card):
  def __init__(self):
    super().__init__("Forest", 7, "Land", 4)
    


  def condition(self, hand):
    for card in hand:
      if card.suit == "Beast" or card.name == "Elven Archers":
        self.total_power += 12
      

    