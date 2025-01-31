from card import Card

class Candle(Card):
  def __init__(self):
    super().__init__("Candle", 2, "Flame", 17)    
    

  @Card.not_blank
  def condition(self, hand):    
    card_combo = {card.name for card in hand}
    if {"Book of Changes", "Bell Tower"}.issubset(card_combo) and any(card.suit == "Wizard" for card in hand):
      self.total_power += 100