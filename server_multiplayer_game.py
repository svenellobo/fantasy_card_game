from deck import Deck
from player import Player
from discard_area import DiscardArea
import random

class ServerMultiplayerGame():
    def __init__(self, player_names: list[str]):
        self.image_paths = []               
        self.deck = Deck()
        for card in self.deck.cards:
            self.image_paths.append(card.image)
        self.discard_area = DiscardArea()
        self.deck.shuffle_deck()
        self.players: dict[str, Player] = {}
        self.game_over = False
        
        
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
    
    @property
    def current_player(self):
        current_name = self.turn_order[self.current_player_index]
        return self.players[current_name]

    def end_turn(self):
        if len(self.discard_area.discard_area_cards) >= 10:            
            self.end_game()
            return       
        self.current_player_index = (self.current_player_index + 1) % len(self.turn_order)
        

    def end_game(self):
        self.game_over = True
        for key,value in self.players.items():
            card_effects = value.penalties_and_conditions(value.cards_in_hand)
            total_score = value.calculate_total_points()
        
        return
        #tu izračunam score
        

    def get_current_player(self):
        return self.players[self.turn_order[self.current_player_index]]
    