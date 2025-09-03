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
    

    def get_current_player(self):
        return self.players[self.turn_order[self.current_player_index]]
    
    
    def discard_card(self, player_name: str, card_name: str):
        player = self.players.get(player_name)
        if not player:
            raise ValueError("Player not found in game.")

        disc_card = next((c for c in player.cards_in_hand if c.name == card_name), None)
        if not disc_card:
            raise ValueError("Card not found in player hand.")

        player.cards_in_hand.remove(disc_card)
        self.discard_area.discard_area_cards.append(disc_card)

        return {"message": f"{disc_card.name} discarded successfully",
                "discard_area": [card.to_dict() for card in self.discard_area.discard_area_cards]}
    
    def draw_card(self, player_name: str):
        player = self.players.get(player_name)
        if not player:
            raise ValueError("Player not found in game.")
        if self.current_player_name != player_name:
            raise ValueError("It's not your turn.")
        card = self.deck.draw_card()
        player.cards_in_hand.append(card)
        return {"card": card.to_dict()}
    
    def take_from_discard(self, player_name: str, card_name: str):
        player = self.players.get(player_name)
        if not player:
            raise ValueError("Player not found in game.")
        disc_card = next((card for card in self.discard_area.discard_area_cards if card.name == card_name), None)
        if not disc_card:
            raise ValueError("Card not found in discard area.")
        player.cards_in_hand.append(disc_card)
        self.discard_area.discard_area_cards.remove(disc_card)
        return {"card": disc_card.to_dict(),
                "discard_area": [card.to_dict() for card in self.discard_area.discard_area_cards]
    }

    def end_turn(self, player_name: str):
        if self.current_player_name != player_name:
            raise ValueError("It is not your turn.")
        
        if len(self.discard_area.discard_area_cards) >= 10:
            return self.end_game()
        self.current_player_index = (self.current_player_index + 1) % len(self.turn_order)
        return {"status": "turn_ended", "next_player_name": self.current_player_name}
    
    def end_game(self):
        self.game_over = True
        for player in self.players.values():
            player.penalties_and_conditions(player.cards_in_hand)
            player.calculate_total_points()
        player_scores = {
            pname: [card.to_score_dict() for card in player.cards_in_hand]
            for pname, player in self.players.items()
        }
        return {"status": "game_over", "player_scores": player_scores}
    