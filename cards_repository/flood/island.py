from card import Card

class Island(Card):
  def __init__(self):
    super().__init__("Island", 14, "Flood", 9)
    self.has_clear = True
    

  @Card.not_blank
  def condition(self, hand):    
    filtered_hand = [card for card in hand if card.original_state["suit"] in {"Flood", "Flame"}]
    max_power_card = max(filtered_hand, key=lambda card: card.original_state["base_power"])
    max_power_card.penalty = False
