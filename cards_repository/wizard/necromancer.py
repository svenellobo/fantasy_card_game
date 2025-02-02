from card import *

class Necromancer(Card):
  def __init__(self):
    super().__init__("Necromancer", 3, WIZARD, 28)     
    


  @Card.not_blank
  def condition(self, hand):    
    pass