from card import Card

class GreatFlood(Card):
  def __init__(self):
    super().__init__("Great Flood", 32, "Flood", 8)
    self.penalty = True
    

  @Card.not_blank
  def condition(self, hand):
    if self.penalty:
      for card in hand:
        if card.suit == "Army" or (card.suit == "Land" and card.name != "Mountain") or (card.suit == "Flame" and card.name != "Lightning"):
          card.blank()