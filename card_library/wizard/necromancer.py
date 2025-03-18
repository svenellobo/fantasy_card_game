from card import *
import copy

class Necromancer(Card):
    def __init__(self):
        super().__init__("Necromancer", 3, WIZARD, 28)
        self.save_original_state()
        
        
    def penalties_and_conditions(self, hand):
        for card in hand:
                card.reset()
                
        for card in hand:
            if card.has_clear:
                card.clear_penalties(hand)
        
        cards_with_blank = []
        for card in hand:
            if card.has_blank and not card.blanks_self: 
                cards_with_blank.append(card)
                     
        if len(cards_with_blank) > 1:
            for card in cards_with_blank:            
                    card.activate_blank(cards_with_blank)
                
        for card in hand:
            if card.has_blank:
                card.activate_blank(hand)
                
        for card in hand:
            if card.has_blank:
                card.activate_blank(hand)
        
        for card in hand:           
            card.condition(hand)        


    @Card.not_blank
    def condition(self, hand,discard_area=None):    
        if discard_area:    
            best_discard_card = None
            best_impact = -float("inf")  
            hand_total_power = sum(card.total_power for card in hand)
            discard_suits = {ARMY, LEADER, WIZARD, BEAST}

            
            for discard_card in discard_area:
                if discard_card.suit in discard_suits:
                    temp_hand = copy.deepcopy(hand)
                    temp_hand.append(discard_card)
                                        
                    self.penalties_and_conditions(temp_hand)              
                    new_total_power = sum(card.total_power for card in temp_hand)
                    impact = new_total_power - hand_total_power

                    if impact > best_impact:
                        best_discard_card = discard_card
                        best_impact = impact

            
            hand.append(best_discard_card)
            discard_area.remove(best_discard_card)
                