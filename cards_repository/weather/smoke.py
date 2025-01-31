from card import Card


class Smoke(Card):
  def __init__(self):
    super().__init__("Smoke", 27, "Weather", 13)
    self.penalty = True    

  @Card.not_blank
  def condition(self, hand):  
    if self.penalty:
      if not any(card.suit == "Flame" for card in hand):
        self.blank()