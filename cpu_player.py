from hand import Hand
import copy

class CPUPlayer(Hand):
    def __init__(self):
          super().__init__()
              


def remove_worst_card(self, hand:list):    
    hand_total_power = sum(card.total_power for card in hand)
    worst_card = None
    worst_impact = float('inf')    
    
    
    for card in hand: 
        hand_copy = copy.deepcopy(hand)       
        hand_copy.remove(card)
        
        for card_copy in hand_copy:
            card_copy.clear_penalties()
        for card_copy in hand_copy:
            card_copy.condition()
                
        copy_total_power = sum(card_copy.total_power for card_copy in hand_copy)
        card.impact = hand_total_power - copy_total_power
        
        if card.impact < worst_impact:
            worst_impact = card.impact
            worst_card = card
            
    if worst_card:
        hand.remove(worst_card)
        
        
            
        #lowest_power =  min(hand, key=lambda card: card.total_power)   
        #min(sum(card.total_power for card in hand_copy) for card in hand)