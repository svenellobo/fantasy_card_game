
class Player():
    def __init__(self):
        self.cards_in_hand = []

    def calculate_total_points(self):    
        return sum(card.total_power for card in self.cards_in_hand)
  
    def deal_hand(self, deck):      
        for i in range(7):
            card = deck.draw_card()
            self.cards_in_hand.append(card)        
    
            
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
            
    