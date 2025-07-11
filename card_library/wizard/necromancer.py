from card import *
import copy

class Necromancer(Card):
    def __init__(self):
        super().__init__("Necromancer", 3, WIZARD, 28)
        self.priority = 6
        self.image = resource_path("images/necromancer.jpeg")
        self.discard_suits = {ARMY, LEADER, WIZARD, BEAST}
        self.save_original_state()
        
    def card_reset(self, hand):
        for card in hand:
            if card.original_state["name"] not in {"Mirage", "Doppelganger", "Shapeshifter"}:
                card.reset()        
        
    def penalties_and_conditions(self, hand):
        cards_with_blank = []
        order_exception = {"Great Flood", "Blizzard", "Wildfire"}
                
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


    @Card.not_blank
    def bonus(self, hand,discard_area=None):        
        
        if discard_area != None:            
            temp_hand = copy.deepcopy(hand) 
            self.card_reset(temp_hand)   
            best_discard_card = None
            best_impact = -float("inf")  
            hand_total_power = sum(card.total_power for card in temp_hand)
            

            
            for discard_card in discard_area:
                if discard_card.suit in self.discard_suits:
                    self.card_reset(temp_hand)                    
                    temp_hand.append(discard_card)
                                        
                    self.penalties_and_conditions(temp_hand)              
                    new_total_power = sum(card.total_power for card in temp_hand)
                    impact = new_total_power - hand_total_power                    
                    discard_card.reset()
                    temp_hand.remove(discard_card)                    

                    if impact > best_impact:                        
                        best_discard_card = discard_card
                        best_impact = impact
                        
            if best_impact > -float("inf") and len(discard_area) >= 6:
                self.total_power += best_impact            
            if len(discard_area) >= 10:
                if best_discard_card in discard_area:     
                    hand.append(best_discard_card)            
                    discard_area.remove(best_discard_card)
                    self.total_power = self.base_power
        
            
        
            
                