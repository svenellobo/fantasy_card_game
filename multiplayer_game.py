from deck import Deck
from player import Player
from discard_area import DiscardArea
import random

class MultiplayerGame():
    def __init__(self, player_names: list[str]):               
        self.deck = Deck()
        self.discard_area = DiscardArea()
        self.deck.shuffle_deck()
        self.players: dict[str, Player] = {}
        
        self.turn_order = player_names.copy()
        random.shuffle(self.turn_order)
        self.current_player_index = 0        

        for name in self.turn_order:
            player = Player()
            player.deal_hand(self.deck)
            self.players[name] = player

    @property
    def current_player_name(self):
        return self.turn_order[self.current_player_index]

    def end_turn(self):       
        self.current_player_index = (self.current_player_index + 1) % len(self.turn_order)
        

    def get_current_player(self):
        return self.players[self.turn_order[self.current_player_index]]
    

    

        
        
        