from card import *
import copy

class Doppelganger(Card):
    def __init__(self):
        super().__init__("Doppelganger", 0, WILD, 53)
        self.priority = 0
        self.save_original_state()
        
        
    def card_reset(self,hand):
        for card in hand:
            card.reset()
        
        
    def penalties_and_conditions(self, hand):
        cards_with_blank = []       
                
                
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
            if card.priority == 3:
                card.bonus(hand)
                card.effect(hand)
                card.penalty(hand)  
        
        for card in hand:
            if card.priority == 1:
                card.bonus(hand)
                card.effect(hand)
                card.penalty(hand)         
        
        
    @Card.not_blank   
    def effect(self, hand):
        self.card_reset(hand)
        temp_hand = copy.deepcopy(hand)
        self.penalties_and_conditions(hand)        
        best_impact = -float("inf")
        best_card_to_copy = None  
        hand_total_power = sum(card.total_power for card in hand)        
        
        
        
        """for temp_card in temp_hand:
            self.card_reset(temp_hand)
            if temp_card is not self: #temp card nikad ne bude self
                self.name = temp_card.name
                self.base_power = temp_card.base_power
                self.suit = temp_card.suit
                self.has_penalty = temp_card.has_penalty
                self.has_blank = temp_card.has_blank
                self.priority = temp_card.priority
                if temp_card.has_penalty: 
                    self.effect = temp_card.condition
                    self.activate_blank = temp_card.activate_blank
                else:
                    self.effect = Card.effect
                    self.activate_blank = Card.activate_blank
                self.penalties_and_conditions(temp_hand) 
                new_total_power = sum(temp_card.total_power for temp_card in temp_hand)
                impact = new_total_power - hand_total_power
                
                if impact > best_impact:
                    best_impact = impact
                    best_card_to_copy = temp_card
            
                
        self.name = best_card_to_copy.name
        self.base_power = best_card_to_copy.base_power
        self.suit = best_card_to_copy.suit
        self.priority = best_card_to_copy.priority
        if best_card_to_copy.has_penalty: 
            self.effect = best_card_to_copy.condition
            self.activate_blank = best_card_to_copy.activate_blank """
               
    
         