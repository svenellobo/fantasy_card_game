import customtkinter as ctk
from screens.main_menu import MainMenu
from player import Player
from cpu_player import CPUPlayer
from deck import Deck
from discard_area import DiscardArea 
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


class App(ctk.CTk):
    
    def __init__(self, title, geo):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")        
        self.geometry(geo)
        self.title(title)       
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.initialize_main_menu()
        
        
        
    def initialize_main_menu(self):
        MainMenu(self)
        
        """if sticky is None:
            component.grid(row=row, column=column, padx=5, pady=5)
        else:
            component.grid(row=row, column=column, padx=5, pady=5, sticky=sticky)"""
        



def main():
    print("Game started")    
    deck = Deck()

    
    
if __name__ == "__main__":
    app = App("Fantasy Realms", "1000x1000")
    app.mainloop()
    #main()
    
    
    

    
    
    
    """deck.shuffle_deck()    
    
    player = CPUPlayer()
    player.deal_hand(deck)"""
    
    
    
    

    """
    dragon = Dragon()
    player.cards_in_hand.append(dragon)
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
    
    """player.penalties_and_conditions(player.cards_in_hand)    
    for card in player.cards_in_hand:
        print(card)    
    ttt = player.calculate_total_points()   
    print(ttt)"""
  
    
     