class Player():
    def __init__(self):
        self.cards_in_hand = []

    def calculate_total_points(self):    
        return sum(card.total_power for card in self.cards_in_hand)
  
    def deal_hand(self, deck):                   
        for i in range(6):
            card = deck.draw_card()
            self.cards_in_hand.append(card)        
    
            
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
            if card.priority == 0:                
                card.effect(hand)
                

        for card in hand:
            if card.priority == 3:
                card.bonus(hand)                
                card.penalty(hand)

        for card in hand:
            if card.priority == 1:                
                card.bonus(hand)                
                card.penalty(hand)
                
                    
        for card in hand:
            if card.original_state["name"] == "Doppelganger":
                card.final_activation(hand)
                
            #card.activate_blank(hand)
            
                
                    
                
                
                
                
                
    """def penalties_and_conditions(self, hand):
        cards_with_blank = []        
        
        for card in hand:
            #if card.original_state["priority"] != 0:
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
            if card.priority == 0:
                card.condition(hand)

        for card in hand:
            if card.priority == 3:
                card.condition(hand)

        for card in hand:
            if card.priority == 1:
                card.condition(hand)"""

            
    