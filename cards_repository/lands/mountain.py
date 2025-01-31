from card import Card


class Mountain(Card):
  def __init__(self):
    super().__init__("Mountain", 9, "Land", 1)
    

  @Card.not_blank
  def condition(self, hand):
    card_names = {card.name for card in hand}
    if {"Smoke", "Wildfire"}.issubset(card_names):
      self.total_power += 50
    for card in hand:
      if card.suit == "Flood":
          card.penalty = False
    
