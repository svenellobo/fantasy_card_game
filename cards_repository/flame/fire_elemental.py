from card import Card

class FireElemental(Card):
  def __init__(self):
    super().__init__("Fire Elemental", 4, "Flame", 20)    
    

  @Card.not_blank
  def condition(self, hand):    
    flame_count = sum(1 for card in hand if card.suit == "Flame") - 1
    self.total_power += flame_count * 15