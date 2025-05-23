from player import Player
import copy

class CPUPlayer(Player):
    def __init__(self):
          super().__init__()
          self.hand_total_power = 0
          self.total_pow_with_disc_card = 0
          
    
    
    def penalties_and_conditions(self, hand):
        cards_with_blank = []
        order_exception = {"Great Flood", "Blizzard", "Wildfire"}        
        
        for card in hand:            
            card.reset()
                
        for card in hand:
            if card.has_clear:
                card.clear_penalties(hand)
        
        
        for card in hand:
            if card.has_blank and not card.blanks_self:                
                cards_with_blank.append(card)
                                
                     
        if len(cards_with_blank) > 1:
            cards_with_blank_names = {card.name for card in cards_with_blank}
            if order_exception.issubset(cards_with_blank_names):            
                for card in cards_with_blank:                
                    if card.name == "Blizzard":
                        card.activate_blank(cards_with_blank)
                for card in cards_with_blank:
                    card.activate_blank(cards_with_blank)                
            else:
                card.activate_blank(cards_with_blank)
                
        for card in hand:
            if card.has_blank:
                card.activate_blank(hand)
                
        for card in hand:
            if card.has_blank:
                card.activate_blank(hand) 
                
        for card in hand:
            if card.priority == 6:
                card.bonus(hand, self.discard_area)                
        
            
        for card in hand:
            if card.priority == 1:                
                card.effect(hand)
        
                
        for card in hand:
            if card.priority == 2:                
                card.effect(hand) 
        
                 
        for card in hand:
            if card.priority == 3:                
                card.effect(hand)
        

        for card in hand:
            if card.priority == 4:
                card.bonus(hand)
        
        
        for card in hand:
            if card.priority == 5:                
                card.bonus(hand)        
            
                
        for card in hand:
            if card.priority == 5:
                card.penalty(hand)        
      
                    
        for card in hand:
            if card.original_state["name"] == "Doppelganger":
                card.final_activation(hand)  
        
        
                
    def remove_worst_card(self, hand: list):        
        worst_impact = float("inf")        
        worst_card = None
        
        for card in hand:
            temp_hand = copy.deepcopy(hand)
            
            card_index = hand.index(card)
            temp_hand.pop(card_index)            
            self.penalties_and_conditions(temp_hand)
            new_power = self.total_pow_with_disc_card - sum(card.total_power for card in temp_hand)
            
            if new_power < worst_impact:
                worst_impact = new_power
                worst_card = card
                
        if worst_card:           
            hand.remove(worst_card)
            return worst_card
        
    
        
    def take_turn(self, deck, discard_area):
        start_len = len(discard_area)                       
        self.penalties_and_conditions(self.cards_in_hand)       
        best_discard_card = None
        best_impact = -float("inf")          
        self.hand_total_power = sum(card.total_power for card in self.cards_in_hand)
               

        if discard_area:
            for discard_card in discard_area:
                temp_hand = copy.deepcopy(self.cards_in_hand)
                temp_hand.append(discard_card)
                self.penalties_and_conditions(temp_hand)
                self.total_pow_with_disc_card = sum(card.total_power for card in temp_hand)
                removed_card = self.remove_worst_card(temp_hand)
                new_total_power = sum(card.total_power for card in temp_hand)                
                impact = new_total_power - self.hand_total_power
                

                if impact > best_impact:
                    best_discard_card = discard_card
                    best_impact = impact
                    
            

        if best_discard_card and best_impact >= 25:            
            self.cards_in_hand.append(best_discard_card)
            discard_area.remove(best_discard_card)
            
        
        else:
            self.cards_in_hand.append(deck.draw_card())
        
        removed_card = self.remove_worst_card(self.cards_in_hand)        
        discard_area.append(removed_card)
        for card in discard_area:
                card.reset()    
        self.hand_total_power = 0
        self.total_pow_with_disc_card = 0
        if start_len == len(discard_area):
            return best_discard_card
        
        
    
        
        
        

        
            
        