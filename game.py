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
from card_library.artifact.book_of_changes import BookOfChanges
from card_library.army.dwarvish_infantry import DwarvishInfantry
from card_library.army.knights import Knights
from card_library.flame.fire_elemental import FireElemental
from card_library.flame.forge import Forge
from card_library.leader.queen import Queen
from card_library.beast.basilisk import Basilisk
from card_library.wizard.beastmaster import Beastmaster
from card_library.land.bell_tower import BellTower
from card_library.flame.wildfire import Wildfire
from card_library.land.mountain import Mountain
from card_library.flood.great_flood import GreatFlood
from card_library.army.elven_archers import ElvenArchers
from card_library.wizard.necromancer import Necromancer
from card_library.flood.water_elemental import WaterElemental
from card_library.beast.hydra import Hydra
from card_library.flame.candle import Candle
from card_library.army.light_cavalry import LightCavalry
from card_library.leader.princess import Princess
from card_library.army.rangers import Rangers
from card_library.weather.rainstorm import Rainstorm
from card_library.wizard.collector import Collector
from card_library.wild.doppelganger import Doppelganger
from card_library.weather.blizzard import Blizzard
from card_library.land.cavern import Cavern
from card_library.artifact.protection_rune import ProtectionRune
from card_library.wild.mirage import Mirage
from card_library.leader.king import King
from card_library.wizard.enchantress import Enchantress
from card_library.artifact.world_tree import WorldTree
from card_library.flood.fountain_of_life import FountainOfLife
from card_library.weapon.warship import Warship
from card_library.weapon.war_dirigible import WarDirigible
from card_library.weather.whirlwind import Whirlwind
from card_library.weapon.sword_of_keth import SwordOfKeth
from card_library.artifact.shield_of_keth import ShieldOfKeth
from card_library.wild.shapeshifter import Shapeshifter
from card_library.beast.dragon import Dragon
from card_library.weather.smoke import Smoke
from card_library.leader.warlord import Warlord
from card_library.weapon.magic_wand import MagicWand
from card_library.flood.island import Island
from card_library.weather.air_elemental import AirElemental
from card_library.land.forest import Forest
from card_library.beast.unicorn import Unicorn
from card_library.wizard.warlock_lord import WarlockLord
from card_library.weapon.elven_longbow import ElvenLongbow
from card_library.leader.empress import Empress




class Game():
    def __init__(self, game_screen): 
        self.image_paths = []       
        self.deck = Deck()
        for card in self.deck.cards:
            self.image_paths.append(card.image)
        self.deck.shuffle_deck()
        self.discard_area = DiscardArea()
        self.player1 = Player()
        self.player2 = CPUPlayer()
        self.player2.discard_area = self.discard_area.discard_area_cards
        self.current_player = None
        self.card_taken = False
        self.card_discarded = False        
        self.game_screen = game_screen

        self.play()
            
        
    def take_card_from_discard(self, card):
        if not self.card_taken:        
            self.discard_area.discard_area_cards.remove(card)
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
            self.game_screen.status_area_lbl.configure(text="HINT: Double click on a card in hand to discard it")
            self.game_screen.draw_button.configure(fg_color="#800000", state="disabled")
            self.card_taken = True
    
    def draw_from_deck(self):
        if self.current_player == "player" and not self.card_taken:        
            card = self.deck.draw_card()
            self.player1.cards_in_hand.append(card)        
            self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
            self.game_screen.status_area_lbl.configure(text="HINT: Double click on an unwanted card in your hand to discard it.")
            self.card_taken = True
            self.game_screen.draw_button.configure(fg_color="#800000", state="disabled")
        
            
        
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
        if any(card.name in {"Mirage", "Doppelganger", "Shapeshifter", "Necromancer", "Book of Changes", "Island"} for card in self.player1.cards_in_hand):
            self.game_screen.open_choice_screen(self.player1, self.player2, self.discard_area)
        else:       
            self.game_screen.open_score_screen(self.player1, self.player2, self.discard_area) 
            
            
        
        
    
    def end_turn(self):
        if self.card_taken and self.card_discarded:
            if len(self.discard_area.discard_area_cards) >= 10:
                self.end_game()
            else: 
                if self.current_player == "player":                
                    self.current_player = "cpu"
                    self.game_screen.after(500, self.cpu_turn_logic())                
                elif self.current_player == "cpu":                
                    self.current_player = "player"
                    self.player_turn_logic()
                
    
    def update_game_screen(self):    
        self.game_screen.display_cards(self.player1.cards_in_hand, "player_hand")
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")

    
    def player_turn_logic(self):        
        self.current_player = "player"
        self.game_screen.end_turn_btn.configure(fg_color="#800000", state="disabled")
        self.game_screen.draw_button.configure(fg_color="green", state="normal")
        self.game_screen.status_area_lbl.configure(text="HINT: Draw a card from the deck or take one from the discard area.")
        self.card_taken = False
        self.card_discarded = False      
        
        
                
                
    def cpu_turn_logic(self):               
        disc_len = len(self.discard_area.discard_area_cards)        
        turn_logic = self.player2.take_turn(self.deck, self.discard_area.discard_area_cards)                
        self.game_screen.display_cards(self.player2.cards_in_hand, "opponent_hand")
        self.game_screen.display_cards(self.discard_area.discard_area_cards, "discard_area")
        if disc_len == len(self.discard_area.discard_area_cards):
            self.game_screen.card_preview(turn_logic.image)       
                
        self.end_turn()
        
            
    
    

    def play(self):
        self.player1.deal_hand(self.deck)
        self.player2.deal_hand(self.deck) 
        self.update_game_screen()
        
        self.player_turn_logic()      
   