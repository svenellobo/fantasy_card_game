from card import Card

class Wildfire(Card):
  def __init__(self):
    super().__init__("Wildfire", 40, "Flame", 16)
    self.penalty = True
    

  @Card.not_blank
  def condition(self, hand):    
    if self.penalty:
      for card in hand:        
        if card.suit not in {"Flame", "Wizard", "Weather", "Weapon", "Artifact"} and card.name not in {"Mountain", "Great Flood", "Island", "Unicorn", "Dragon"}:
          card.blank()