from card import Card

class Forge(Card):
  def __init__(self):
    super().__init__("Forge", 9, "Flame", 18)    
    

  @Card.not_blank
  def condition(self, hand):    
    count = sum(1 for card in hand if card.suit == "Artifact" or card.suit == "Weapon")
    self.total_power += count * 9