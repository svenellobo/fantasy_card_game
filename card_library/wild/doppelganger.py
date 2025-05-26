from card import *
import copy


class Doppelganger(Card):
    def __init__(self):
        super().__init__("Doppelganger", 0, WILD, 53)
        self.priority = 1        
        self.image = resource_path("images/doppelganger.jpeg")
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

        for card in hand:
            if card.priority == 4:                               
                card.bonus(hand)
        
        for card in hand:
            if card.priority == 5:                
                card.penalty(hand)                
                card.bonus(hand)
                
                
                 
                
    def final_activation(self, hand):        
        for card in hand:
            if card.original_state["name"] == self.name and card.original_state["name"] != "Doppelganger":                
                if card.name == "Basilisk" and card.has_penalty:
                    self.blank()
                    if card.suit in {ARMY, LEADER, BEAST}:
                        card.blank()
                    
                else:                                        
                    self.name = card.original_state["name"]                                        
                    self.suit = card.original_state["suit"]                    
                    self.has_penalty = card.has_penalty
                    self.has_blank = card.has_blank
                    self.base_power = card.base_power                        
                    self.is_blanked = card.is_blanked
                    if self.is_blanked:
                        self.blank()                    
                    if card.has_blank and not any(card.original_state["name"] == "Protection Rune" for card in hand):
                        card.has_penalty = True
                        card.activate_blank(hand)
                        card.has_penalty = False
                    if card.total_power < card.base_power:
                        self.total_power = card.total_power                        
                    else:
                        self.total_power = card.base_power 
                
    
            
    def best_card_to_copy(self, best_card): 
        self.name = best_card.original_state["name"]
        self.base_power = best_card.base_power
        self.total_power = best_card.base_power
        self.suit = best_card.original_state["suit"]            
        self.has_penalty = best_card.has_penalty
        self.has_blank = best_card.has_blank
        
                            
                            
       
    def effect(self, hand):
        best_card = None
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
            if temp_card.has_penalty and not temp_card.is_blanked:
                dop_card.total_power = temp_card.total_power

            if temp_card.has_blank and not any(card.original_state["name"] == "Protection Rune" for card in hand):                
                temp_card.has_penalty = True
                temp_card.activate_blank(hand)
                temp_card.has_penalty = False

            if temp_card.is_blanked:
                dop_card.total_power = 0
            
            
            new_total_power = sum(card.total_power for card in temp_hand)
            impact = new_total_power - hand_total_power
            
            if impact > best_impact:    
                best_impact = impact                
                for card in hand:
                    if temp_card.original_state["name"] == card.original_state["name"]:
                        best_card = card
                
            self.card_reset(temp_hand)
                
            
               
        self.best_card_to_copy(best_card)   
    
  