from card import *
import copy

class Doppelganger(Card):
    def __init__(self):
        super().__init__("Doppelganger", 0, WILD, 53)
        self.save_original_state()
        
        
    def penalties_and_conditions(self, hand):
        cards_with_blank = []        
        
        for card in hand:
                card.reset()
                
        for card in hand:
            if card.has_clear:
                card.clear_penalties(hand)
        
        
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
            if card.priority == 1:
                card.condition(hand)
        
        for card in hand:
            if card.priority == 3:
                card.condition(hand)        
        
        
    @Card.not_blank   
    def condition(self, hand):        
        best_impact = -float("inf")  
        hand_total_power = sum(card.total_power for card in hand)
        
        
        
        temp_hand = copy.deepcopy(hand)
        for temp_card in temp_hand:
            self.name = temp_card.name
            self.base_power = temp_card.base_power
            self.suit = temp_card.suit
            if temp_card.has_penalty: #možda originalni has_penalty iz dict
                self.condition = temp_card.condition
                 
        if hasattr(self, 'condition') and callable(self.condition):
            self.condition(hand)
        
    
        pass 