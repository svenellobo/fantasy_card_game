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
        
        """
        
        mnt = Mountain()
        self.player2.cards_in_hand.append(mnt)
        
        flood = GreatFlood()
        self.player2.cards_in_hand.append(flood)
        
        smoke = Smoke()
        self.player2.cards_in_hand.append(smoke)
        
        forge = Forge()
        self.player2.cards_in_hand.append(forge)
        
        hyd = Hydra()
        self.player2.cards_in_hand.append(hyd)
        
        warship = Warship()
        self.player2.cards_in_hand.append(warship)
        
        wtree = WorldTree()
        self.player2.cards_in_hand.append(wtree)"""
        
              
        
        boc = BookOfChanges()
        self.player1.cards_in_hand.append(boc)        
        self.player1.cards_in_hand.append(necro)
        dop = Doppelganger()
        self.player1.cards_in_hand.append(dop)
        mirage = Mirage()
        self.player1.cards_in_hand.append(mirage)
        shape = Shapeshifter()
        self.player1.cards_in_hand.append(shape)
        bas = Basilisk()
        self.player1.cards_in_hand.append(bas)
        
        
        
        wildfire = Wildfire()
        self.player2.cards_in_hand.append(wildfire)
        
        
        """dragon = Dragon()
        player.cards_in_hand.append(dragon)
        magicwand = MagicWand()
        self.player2.cards_in_hand.append(magicwand)
        lightcaval = LightCavalry()
        player.cards_in_hand.append(lightcaval)
        shape = Shapeshifter()
        player.cards_in_hand.append(shape)
        sword = SwordOfKeth()
        player.cards_in_hand.append(sword)    
        shield = ShieldOfKeth()
        player.cards_in_hand.append(shield)
        cavern = Cavern()
        player.cards_in_hand.append(cavern)
        wardirigble = WarDirigible()
        player.cards_in_hand.append(wardirigble)
        warship = Warship()
        player.cards_in_hand.append(warship)
        ranger = Rangers()
        player.cards_in_hand.append(ranger)
        fontana = FountainOfLife()
        player.cards_in_hand.append(fontana)
        wtree = WorldTree()
        player.cards_in_hand.append(wtree)
        enchant = Enchantress()
        player.cards_in_hand.append(enchant)
        blizz = Blizzard()
        player.cards_in_hand.append(blizz)
        king = King()
        player.cards_in_hand.append(king)
        mirage = Mirage()
        player.cards_in_hand.append(mirage)
        prorune = ProtectionRune()
        player.cards_in_hand.append(prorune)
        wildfire = Wildfire()
        player.cards_in_hand.append(wildfire)
        kn = Knights()
        player.cards_in_hand.append(kn)
        fe = FireElemental()
        player.cards_in_hand.append(fe) 
        forge = Forge()
        player.cards_in_hand.append(forge)
        qu = Queen()
        player.cards_in_hand.append(qu)
        bas = Basilisk()
        player.cards_in_hand.append(bas)
        beastmas = Beastmaster()
        player.cards_in_hand.append(beastmas)
        bell = BellTower()
        player.cards_in_hand.append(bell)    
        forge = Forge()
        player.cards_in_hand.append(forge)
        boc = BookOfChanges()
        player.cards_in_hand.append(boc)
        mnt = Mountain()
        player.cards_in_hand.append(mnt)
        dop = Doppelganger()
        player.cards_in_hand.append(dop)
        flood = GreatFlood()
        player.cards_in_hand.append(flood)
        arch = ElvenArchers()
        player.cards_in_hand.append(arch)
        dw = DwarvishInfantry()
        player.cards_in_hand.append(dw)
        necro = Necromancer() 
        player.cards_in_hand.append(necro)
        wele = WaterElemental()
        player.cards_in_hand.append(wele)
        hyd = Hydra()
        player.cards_in_hand.append(hyd)
        candle = Candle()
        player.cards_in_hand.append(candle)  """  
           

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
        self.game_screen.end_turn_btn.configure(fg_color="#800000", state="disabled")
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
   