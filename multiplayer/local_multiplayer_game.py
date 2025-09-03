from discard_area import DiscardArea
from constants import SERVER_URL
import requests
from card import Card
from deck import Deck

class LocalMultiplayerGame():
    def __init__(self, mp_game_screen, player_name, room_name):        
        self.discard_area = DiscardArea()
        self.player_name = player_name
        self.room_name = room_name
        self.current_player = None
        self.mp_game_screen = mp_game_screen  

        self.card_taken = False
        self.card_discarded = False      

        self.player_hand = []



    def draw_from_deck(self):
        if self.current_player == self.player_name and not self.card_taken:        
            response = requests.post(f"{SERVER_URL}/draw_card", params={"room_name": self.room_name, "player_name":self.player_name})
            if response.status_code != 200:
                print("Error drawing card:", response.text)
                return None 
            
            data = response.json()
            card = Card.from_dict(data["card"])

            self.player_hand.append(card)   
            self.mp_game_screen.display_cards(self.player_hand, "player_hand")
            self.mp_game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.card_taken = True
            self.mp_game_screen.draw_button.configure(fg_color="#800000", state="disabled")

    def discard_from_hand(self, card: Card):
        if self.card_taken and not self.card_discarded:
            response = requests.post(f"{SERVER_URL}/discard_card", params={"room_name": self.room_name, "player_name": self.player_name, "card_name": card.name})

            if response.status_code != 200:
                print("Error discarding card:", response.text)
                return None
            
            data = response.json()

            
            self.player_hand.remove(card)
            
            self.discard_area.discard_area_cards = [Card.from_dict(c) for c in data["discard_area"]]
            card.reset()
            
            self.mp_game_screen.display_cards(self.player_hand, "player_hand")
            self.mp_game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_discarded = True
            if len(self.discard_area.discard_area_cards) < 10:
                self.mp_game_screen.end_turn_btn.configure(fg_color="green", state="normal")            
                self.mp_game_screen.status_area_lbl.configure(text="END TURN: Click on the 'End Turn' button")
            else:
                self.mp_game_screen.end_turn_btn.configure(fg_color="green", state="normal", text="End Game")
                self.mp_game_screen.status_area_lbl.configure(text="END GAME: Click on the 'End Game' button")

    

    def take_card_from_discard(self, card):
        if self.current_player == self.player_name and not self.card_taken:
            response = requests.post(f"{SERVER_URL}/take_from_discard", params={"room_name": self.room_name, "player_name": self.player_name, "card_name": card.name})

            if response.status_code != 200:
                print("Error discarding card:", response.text)
                return None 

            data = response.json()
            taken_card = Card.from_dict(data["card"])
            self.player_hand.append(taken_card)
            self.discard_area.discard_area_cards = [Card.from_dict(c) for c in data["discard_area"]]
                    
            self.mp_game_screen.display_cards(self.player_hand, "player_hand")
            self.mp_game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.mp_game_screen.status_area_lbl.configure(text="DISCARD PHASE: Double-click on an unwanted card in your hand to discard it.")
            self.mp_game_screen.draw_button.configure(fg_color="#800000", state="disabled")
            self.card_taken = True
    
    
            
    def end_turn(self):
        self.mp_game_screen.end_turn_btn.configure(state="disabled", fg_color="#800000")

        response = requests.post(f"{SERVER_URL}/end_turn", params={"room_name": self.room_name, "player_name": self.player_name})
        if response.status_code != 200:
            print("Error ending turn:", response.text)
            return

        data = response.json()
        status = data.get("status")

        if status == "turn_ended":
            next_player_name = data.get("next_player_name")
            self.current_player = next_player_name
            self.mp_game_screen.current_player_lbl.configure(text=f"Turn: {self.current_player}")

        elif status == "game_over":
            player_scores = data.get("player_scores", {})
            #tu ide choice screen
    
              
        
    def end_game(self):
        response = requests.post(f"{SERVER_URL}/end_game", params={"room_name": self.room_name})
        if response.status_code != 200:
            print("Error ending game:", response.text)
            return
        data = response.json()                
        player_scores = data.get("player_scores", {})
        #create a ctk.Frame screen for displaying points



        """if any(card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes", "Island"} for card in self.player1.cards_in_hand):
            self.game_screen.open_choice_screen(self.player1, self.player2, self.discard_area)
        else:       
            self.game_screen.open_score_screen(self.player1, self.player2, self.discard_area) """
            
            
        
        
    
    
                
    
    """def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):               
        self.current_player = "player"
        self.game_screen.end_turn_btn.configure(fg_color="#800000", state="disabled")
        self.game_screen.draw_button.configure(fg_color="green", state="normal")
        self.game_screen.status_area_lbl.configure(text="DRAW PHASE: Draw from the deck or double-click a discard area card to take it.")
        self.card_taken = False
        self.card_discarded = False
    """

    

        
        
        