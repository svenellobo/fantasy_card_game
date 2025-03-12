from hand import Hand
import copy

class CPUPlayer(Hand):
    def __init__(self):
          super().__init__()
              

            
    def remove_worst_card(self, hand: list):    
        hand_total_power = sum(card.total_power for card in hand)

        def calculate_impact(card_to_remove):
            hand_copy = copy.deepcopy(hand)
            hand_copy.remove(next(c for c in hand_copy if c.name == card_to_remove.name))
            
            for card_copy in hand_copy:
                card_copy.clear_penalties()
            for card_copy in hand_copy:
                card_copy.condition()

            return hand_total_power - sum(card_copy.total_power for card_copy in hand_copy)

        worst_card = min(hand, key=calculate_impact, default=None)

        if worst_card:
            hand.remove(worst_card)
        
            
        