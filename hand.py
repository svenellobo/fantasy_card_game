

class Hand():
  def __init__(self):
    self.cards_in_hand = []

  def calculate_total_points(self):    
    return sum(card.power for card in self.cards_in_hand)
  
  