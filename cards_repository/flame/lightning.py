from card import Card

class Lightning(Card):
  def __init__(self):
    super().__init__("Lightning", 11, "Flame", 19)    
    

  @Card.not_blank
  def condition(self, hand):    
    if any(card.name == "Rainstorm" for card in hand):
      self.total_power += 30