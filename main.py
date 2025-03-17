from player import Player
from cpu_player import CPUPlayer
from deck import Deck


def main():
    print("Game started")    
    deck = Deck()
    deck.shuffle_deck()    
    
    player = CPUPlayer()
    player.deal_hand(deck)
    
    player.penalties_and_conditions(player.cards_in_hand)
    for card in player.cards_in_hand:
        print(card)
    for card in player.cards_in_hand:
        print(card.has_penalty)
    ttt = player.calculate_total_points()   
    print(ttt)   
    
    
    

if __name__ == "__main__":
    main()