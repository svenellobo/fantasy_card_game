from card_library.artifact.book_of_changes import BookOfChanges
class Player():
    def __init__(self):
        self.cards_in_hand = []

    def calculate_total_points(self):    
        return sum(card.total_power for card in self.cards_in_hand)
  
    def deal_hand(self, deck):
        wt = BookOfChanges()
        self.cards_in_hand.append(wt)      
        for i in range(6):
            card = deck.draw_card()
            self.cards_in_hand.append(card)        
    
            
    def penalties_and_conditions(self, hand):
        cards_with_blank = []
        cards_with_self_blanking = []
        
        for card in hand:
                card.reset()
                
        for card in hand:
            if card.has_clear:
                card.clear_penalties(hand)
        
        
        for card in hand:
            if card.has_blank:
                if not card.blanks_self: 
                    cards_with_blank.append(card)
                if card.blanks_self:
                    cards_with_self_blanking.append(card)
                     
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
            if card not in cards_with_self_blanking:         
                card.condition(hand)
        
        for card in cards_with_self_blanking:
            card.condition(hand)
            
            
    