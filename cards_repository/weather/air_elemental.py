from card import Card


class AirElemental(Card):
  def __init__(self):
    super().__init__("Air Elemental", 4, "Weather", 15)
       

  @Card.not_blank
  def condition(self, hand):  
    weather_count = sum(1 for card in hand if card.suit == "Weather") - 1
    self.total_power += weather_count * 15