from card import *
import copy
import types

class Doppelganger(Card):
    def __init__(self):
        super().__init__("Doppelganger", 0, WILD, 53)
        self.priority = 1
        self.best_card = None
        self.image = "images/doppelganger.jpeg"
        self.save_original_state()
        
        
    def card_reset(self, hand):
        for card in hand:
            if card.original_state["name"] not in {"Mirage", "Doppelganger", "Shapeshifter"}:
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
                
        """for card in hand:
            if card.priority == 2:
                card.effect(hand)
                
        for card in hand:
            if card.priority == 3:
                card.effect(hand)"""

        for card in hand:
            if card.priority == 4:                               
                card.bonus(hand)
        
        for card in hand:
            if card.priority == 5:                
                card.penalty(hand)                
                card.bonus(hand)               
                 
                
    
            
    def best_card_to_copy(self):
        if self.best_card:
            self.name = self.best_card.name
            self.base_power = self.best_card.base_power
            self.total_power = self.best_card.base_power
            self.suit = self.best_card.suit
            self.priority = self.best_card.priority
            self.has_penalty = self.best_card.has_penalty
            self.has_blank = self.best_card.has_blank
            
            
            
    def final_activation(self, hand):          
        if self.original_state["name"] == "Doppelganger":
            self.reset()
        else:
            for card in hand:
                if self.best_card:
                    if card.original_state["name"] == self.best_card.name:
                        if card.name == "Basilisk" and card.has_penalty:
                            card.blank()
                            self.blank()
                        else:                                        
                            self.name = card.name                                        
                            self.suit = card.suit
                            self.priority = card.priority
                            self.has_penalty = card.has_penalty
                            self.has_blank = card.has_blank
                            self.base_power = card.base_power                        
                            self.is_blanked = card.is_blanked
                            if card.total_power < card.base_power:
                                self.total_power = card.total_power                        
                            else:
                                self.total_power = card.base_power
                             
                            
       
    def effect(self, hand):
        temp_hand = copy.deepcopy(hand)
        self.card_reset(temp_hand)        
        self.penalties_and_conditions(temp_hand)        
        best_impact = -float("inf")              
        hand_total_power = sum(card.total_power for card in temp_hand)
        self.card_reset(temp_hand)
        
        for temp_card in temp_hand:
            if temp_card.original_state["name"] == "Doppelganger":
                dop_card = temp_card
        
        
        for temp_card in temp_hand:                    
                dop_card.name = temp_card.name
                dop_card.base_power = temp_card.base_power
                dop_card.total_power = temp_card.total_power
                dop_card.suit = temp_card.original_state["suit"]
                dop_card.has_penalty = temp_card.has_penalty
                dop_card.has_blank = temp_card.has_blank                    
                dop_card.is_blanked = temp_card.is_blanked  
                self.penalties_and_conditions(temp_hand)
                if temp_card.has_penalty and not temp_card.has_blank:
                    dop_card.total_power = temp_card.total_power
                    
                if temp_card.is_blanked:
                    dop_card.total_power = 0
                
                
                new_total_power = sum(card.total_power for card in temp_hand)
                impact = new_total_power - hand_total_power
                
                if impact > best_impact:
                    best_impact = impact
                    self.best_card = temp_card
                self.card_reset(temp_hand)
            
                
        self.best_card_to_copy()   
    
  