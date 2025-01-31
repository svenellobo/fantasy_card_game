from card import Card


class Blizzard(Card):
  def __init__(self):
    super().__init__("Blizzard", 30, "Weather", 12)
    self.penalty = True    

  @Card.not_blank
  def condition(self, hand):  
    if self.penalty:
      for card in hand:
        if card.suit == "Flood":
          card.blank()
          
    count = sum(1 for card in hand if card.suit in {"Army", "Leader", "Beast", "Flame"})
    self.total_power += count * -5