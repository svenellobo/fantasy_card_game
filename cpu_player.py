from player import Player
import copy

class CPUPlayer(Player):
    def __init__(self):
          super().__init__()
              

            
    def remove_worst_card(self, hand: list):
        self.penalties_and_conditions(hand)
        hand_total_power = sum(card.total_power for card in hand)
        worst_impact = float("inf")
        worst_card = None
        
        for card in hand:
            temp_hand = copy.deepcopy(hand)
            temp_hand.remove(card)
            self.penalties_and_conditions(temp_hand)
            new_power = hand_total_power - sum(card.total_power for card in temp_hand)
            
            if new_power < worst_impact:
                worst_impact = new_power
                worst_card = card
        
        if worst_card:            
            hand.remove(worst_card)
            return worst_card          
    
        
    def take_turn(self, deck, discard_area): 
        self.penalties_and_conditions(deck)       
        best_discard_card = None
        best_impact = -float("inf")          
        hand_total_power = sum(card.total_power for card in self.cards_in_hand)

        if discard_area:
            for discard_card in discard_area:
                temp_hand = copy.deepcopy(self.cards_in_hand)
                temp_hand.append(discard_card)  
                
                removed_card = self.remove_worst_card(temp_hand)
                new_total_power = sum(card.total_power for card in temp_hand)
                impact = new_total_power - hand_total_power

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
        
    
        
        
        

        
            
        