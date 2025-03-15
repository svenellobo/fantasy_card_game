from card_library.land.mountain import Mountain
from player import Player
from cpu_player import CPUPlayer
from deck import Deck
from card_library.weather.smoke import Smoke

def main():
    print("Game started")
    """test = Mountain()
    print(test)
    print(test.total_power)
    test2 = Smoke()
    print(test2)"""
    deck = Deck()
    deck.shuffle_deck()    
    """for card in deck.cards:
        print(card)    
    print(len(deck.cards))"""
    player = CPUPlayer()
    player.deal_hand(deck)
    
    player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        print(card)
    for card in player.cards_in_hand:
        print(card.has_penalty)
    ttt = player.calculate_total_points    
    print(ttt)
    
    

if __name__ == "__main__":
    main()