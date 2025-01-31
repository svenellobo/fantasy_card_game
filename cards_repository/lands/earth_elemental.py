from card import Card


class EarthElemental(Card):
  def __init__(self):
    super().__init__("Earth Elemental", 4, "Land", 5)    

  @Card.not_blank
  def condition(self, hand):
    land_count = sum(1 for card in hand if card.suit == "Land") - 1
    self.total_power += land_count * 15
    
    