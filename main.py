from player import Player
from cpu_player import CPUPlayer
from deck import Deck
from discard_area import DiscardArea
from card_library.beast.unicorn import Unicorn
from card_library.army.rangers import Rangers
from card_library.land.earth_elemental import EarthElemental


def main():
    print("Game started")    
    deck = Deck()
    
    for card in deck.cards:
        if card.name == "Rangers" or card.name == "Unicorn" or card.name == "Necromancer" or card.name == "Earth Elemental":
            deck.cards.remove(card)
    
    deck.shuffle_deck()    
    
    player = CPUPlayer()
    player.deal_hand(deck)
    
    ranger = Rangers()
    uni = Unicorn()
    ele = EarthElemental()
    
    discard_area = DiscardArea()
    discard_area.discard_area_cards.append(ranger)
    discard_area.discard_area_cards.append(uni)  
    discard_area.discard_area_cards.append(ele)  
    
    player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        if card.name == "Necromancer":
            card.condition(player.cards_in_hand, discard_area=discard_area.discard_area_cards)
    
    player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        print(card)
    for card in player.cards_in_hand:
        print(card.has_penalty)
    ttt = player.calculate_total_points()   
    print(ttt)   
    
    for card in discard_area.discard_area_cards:
        print(f"DISCARD AREA CARD {card.name}")
    
    
    
if __name__ == "__main__":
    main()