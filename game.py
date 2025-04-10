from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea
from screens.game_screen import GameScreen
from screens.card_widget import CardWidget


from card_library.beast.dragon import Dragon
from card_library.army.light_cavalry import LightCavalry



class Game():
    def __init__(self, game_screen):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = Player()
        self.player2 = CPUPlayer()
        self.discard_area = DiscardArea()
        self.player_turn = False
        self.cpu_player_turn = False
        self.card_taken = False
        self.card_discarded = False
        
        dragon = Dragon()
        self.discard_area.discard_area_cards.append(dragon)
        lightcaval = LightCavalry()
        self.discard_area.discard_area_cards.append(lightcaval)
        
        """self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon)"""
        
        
                      
        self.game_screen = game_screen        
        
        """self.player1.deal_hand(self.deck) 
        self.player2.deal_hand(self.deck)"""
        
        
        
        self.play()
            
        
    def take_card_from_discard(self, card):
        if not self.card_taken:        
            self.discard_area.discard_area_cards.remove(card)
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.player_turn and not self.card_taken:        
            card = self.deck.draw_card()
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.card_taken = True
        else:
            print("already drew")
        
    def discard_from_hand(self, card):
        if self.card_taken and not self.card_discarded:            
            self.player1.cards_in_hand.remove(card)
            self.discard_area.discard_area_cards.append(card)
            card.reset()
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.card_discarded = True
            print(f"discard card: {self.card_taken}")
        
    def is_game_over(self, discard_area):
        if len(discard_area) >= 10:
            return True
        return False
    
    def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):
        print("Player 1's turn...")
        self.player_turn = True
        self.card_taken = False
        self.card_discarded = False
        
        
        if self.card_taken and self.card_discarded:
            self.player_turn = False
            self.cpu_player_turn = True
            self.game_screen.end_turn_btn.configure(fg_color="red")
                
                
    def cpu_turn_logic(self):
        print("CPU Player's turn...")
        self.player2.take_turn(self.deck, self.discard_area.discard_area_cards)
        self.player_turn = True
        self.cpu_player_turn = False
            
    
    

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck) 
        self.update_game_screen()
        
        self.player_turn_logic()
        
        
        """ while not self.is_game_over(self.discard_area.discard_area_cards):
            self.player_turn_logic()
            
            if self.is_game_over(self.discard_area.discard_area_cards):  
                break
                
            self.cpu_turn_logic()
            if self.is_game_over(self.discard_area.discard_area_cards):  
                break"""
        
        
        """for card in self.player1.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player1.cards_in_hand, discard_area=self.discard_area.discard_area_cards)
                
        for card in self.player2.cards_in_hand:
            if any(card.name == "Necromancer"):
                card.bonus(self.player2.cards_in_hand, discard_area=self.discard_area.discard_area_cards)"""
        
                
        
        """player1_score = self.player1.calculate_total_points(self.player1.cards_in_hand) 
        player2_score = self.player2.calculate_total_points(self.player2.cards_in_hand)
        print(f"Player 1 Score: {player1_score}") 
        print(f"Player 2 Score: {player2_score}") """
    
    
        #draw a card
        #select a card to discard
        #table list append card that's discarded
        #player 2 turn
        #draw a card or take one from table
        #analyze cards on a table and if value added is >= 25 takes that card from table
        #remove worst card    
            
    
        

    