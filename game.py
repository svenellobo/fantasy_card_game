from deck import Deck
from player import Player
from cpu_player import CPUPlayer
from discard_area import DiscardArea
from gui.game_screen import GameScreen
from gui.card_widget import CardWidget
from gui.score_screen import ScoreScreen
from card_library.beast.dragon import Dragon
from card_library.wild.doppelganger import Doppelganger
from card_library.wild.mirage import Mirage
from card_library.wild.shapeshifter import Shapeshifter
from card_library.artifact.book_of_changes import BookOfChanges
from card_library.wizard.necromancer import Necromancer




class Game():
    def __init__(self, game_screen):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player1 = Player()
        self.player2 = CPUPlayer()
        self.discard_area = DiscardArea()
        self.current_player = None
        self.card_taken = False
        self.card_discarded = False        
        self.game_screen = game_screen
           
        necro = Necromancer() 
        dragon = Dragon()
        self.discard_area.discard_area_cards.append(dragon)
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(dragon) 
        self.discard_area.discard_area_cards.append(necro) 
        
        boc = BookOfChanges()
        self.player1.cards_in_hand.append(boc)
        
        self.player1.cards_in_hand.append(necro)
        dop = Doppelganger()
        self.player1.cards_in_hand.append(dop)
        mirage = Mirage()
        self.player1.cards_in_hand.append(mirage)
        shape = Shapeshifter()
        self.player1.cards_in_hand.append(shape)
           

        self.play()
            
        
    def take_card_from_discard(self, card):
        if not self.card_taken:        
            self.discard_area.discard_area_cards.remove(card)
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on a card in hand to discard it")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.current_player == "player" and not self.card_taken:        
            card = self.deck.draw_card()
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on an unwanted card in your hand to discard it.")
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
            self.game_screen.end_turn_btn.configure(fg_color="green", state="normal")
            self.game_screen.status_area_lbl.configure(text="HINT: Click on the 'End Turn' button")
               
              
        
    def end_game(self):
        print("game ended")
        #self.destroy()
        if any(card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes"} for card in self.player1.cards_in_hand):
            self.game_screen.open_choice_screen(self.player1, self.player2, self.discard_area)
        else:       
            self.game_screen.open_score_screen(self.player1, self.player2) 
            
            
        
        
    
    def end_turn(self):
        if self.card_taken and self.card_discarded:
            if len(self.discard_area.discard_area_cards) >= 10:
                self.end_game()
            else: 
                if self.current_player == "player":                
                    self.current_player = "cpu"
                    self.game_screen.after(1000, self.cpu_turn_logic())                
                elif self.current_player == "cpu":                
                    self.current_player = "player"
                    self.player_turn_logic()
                
    
    def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):
        print("Player 1's turn...")
        self.current_player = "player"
        self.game_screen.end_turn_btn.configure(fg_color="red", state="disabled")
        self.game_screen.status_area_lbl.configure(text="HINT: Draw a card from the deck or take one from the discard area.")
        self.card_taken = False
        self.card_discarded = False      
        
        
                
                
    def cpu_turn_logic(self):
        print("CPU Player's turn...")
        self.player2.take_turn(self.deck, self.discard_area.discard_area_cards)
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
        self.end_turn()
        
            
    
    

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck) 
        self.update_game_screen()
        
        self.player_turn_logic()        
       
    
    
        #draw a card
        #select a card to discard
        #table list append card that's discarded
        #player 2 turn
        #draw a card or take one from table
        #analyze cards on a table and if value added is >= 25 takes that card from table
        #remove worst card    
            
    
        

    