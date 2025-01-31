from card import Card


class WaterElemental(Card):
  def __init__(self):
    super().__init__("Water Elemental", 4, "Flood", 10)    

  @Card.not_blank
  def condition(self, hand):
    flood_count = sum(1 for card in hand if card.suit == "Flood") - 1
    self.total_power += flood_count * 15