
class Player():
    def __init__(self):
        self.cards_in_hand = []
        self.discard_area = None

    def calculate_total_points(self):    
        return sum(card.total_power for card in self.cards_in_hand)
  
    def deal_hand(self, deck):                   
        for i in range(0):
            card = deck.draw_card()
            self.cards_in_hand.append(card)        
    
            
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
                
                
  
    