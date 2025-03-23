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
from card_library.wild.doppelganger import Doppelganger
from card_library.land.mountain import Mountain
from card_library.flood.great_flood import GreatFlood
from card_library.army.elven_archers import ElvenArchers
from card_library.wizard.necromancer import Necromancer
from card_library.flood.water_elemental import WaterElemental
from card_library.beast.hydra import Hydra
from card_library.flame.candle import Candle
from card_library.army.light_cavalry import LightCavalry
from card_library.leader.princess import Princess



def main():
    print("Game started")    
    deck = Deck()

    
    
    for card in deck.cards:
        if card.name == "Book of Changes":
            deck.cards.remove(card)
    
    deck.shuffle_deck()    
    
    player = CPUPlayer()
    player.deal_hand(deck) 

    

    """

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
    player.cards_in_hand.append(candle)
    """

    
    
    boc = BookOfChanges()
    player.cards_in_hand.append(boc)
    
    lcavl = LightCavalry()
    player.cards_in_hand.append(lcavl)
    
    fe = FireElemental()
    player.cards_in_hand.append(fe)
    
    forge = Forge()
    player.cards_in_hand.append(forge)
    
    candle = Candle()
    player.cards_in_hand.append(candle)
    
    princess = Princess()
    player.cards_in_hand.append(princess)
    
    dw = DwarvishInfantry()
    player.cards_in_hand.append(dw)
    
    
    






    #TESTIRATI BOOK OF CHANGES S DRUGIM KARTAMA KOJE IMAJU SLIČAN SUSTAV KO DWARVEN INFANTRY
    
    
     
    
    """player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        if card.name == "Necromancer":
            card.condition(player.cards_in_hand, discard_area=discard_area.discard_area_cards)"""
    
    player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        print(card)    
    ttt = player.calculate_total_points()   
    print(ttt)   
    
    
    
    
    
if __name__ == "__main__":
    main()