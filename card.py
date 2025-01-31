class Card():
  def __init__(self, name, power, suit, card_nmb):
    self.name = name
    self.base_power = power
    self.total_power = self.base_power
    self.suit = suit
    self.card_nmb = card_nmb    
    self.penalty = False
    self.has_clear = False
    self.is_blanked = False

    self.original_state = {
            "name": name,
            "base_power": power,
            "suit": suit,
            "card_nmb": card_nmb,
            "total_power": self.total_power,
            "penalty": self.penalty,
            "has_clear": self.has_clear,
            "is_blanked": self.is_blanked
        }

  def __str__(self):
    return f"Card {self.card_nmb} {self.name} belongs to {self.suit} suit and has base power of {self.base_power}" 
  

  def blank(self):
    self.name = None
    self.suit = None
    self.base_power = 0
    self.total_power = 0    
    self.penalty = False
    self.is_blanked = True

   
  def reset(self):        
    self.name = self.original_state["name"]
    self.base_power = self.original_state["base_power"]
    self.suit = self.original_state["suit"]
    self.card_nmb = self.original_state["card_nmb"]
    self.total_power = self.original_state["total_power"]
    self.penalty = self.original_state["penalty"]
    self.is_blanked = self.original_state["is_blanked"]

  #decorator for checking if card is blanked
  def not_blank(func):
    def wrapper(self, *args, **kwargs):
      if self.is_blanked:
          return 
      return func(self, *args, **kwargs)
    return wrapper