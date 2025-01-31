from card import Card

class Swamp(Card):
  def __init__(self):
    super().__init__("Swamp", 18, "Flood", 7)
    self.penalty = True
    

  @Card.not_blank
  def condition(self, hand):
    if self.penalty:
      count = sum(1 for card in hand if card.suit in {"Army", "Flame"})
      self.total_power -= count * 3