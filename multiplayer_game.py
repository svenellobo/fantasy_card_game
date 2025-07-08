from deck import Deck
from player import Player
from discard_area import DiscardArea

import random
import server





class MultiplayerGame():
    def __init__(self, game_screen):               
        self.deck = Deck()
        self.discard_area = DiscardArea()
        
        
        