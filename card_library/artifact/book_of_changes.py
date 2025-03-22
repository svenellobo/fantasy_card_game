from card import *
import copy

class BookOfChanges(Card):
    def __init__(self):
        super().__init__("Book of Changes", 3, ARTIFACT, 49)
        self.priority = 3
        self.save_original_state()
        
    def card_reset(self,hand):
        for card in hand:
            card.reset()
    
        
    def penalties_and_conditions(self, hand):
        cards_with_blank = []
        cards_with_self_blanking = []        
       
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
            if card.priority == 1:
                card.condition(hand)
            """if card.priority == 3:
                card.condition(hand)"""       
        
        
        
        
    @Card.not_blank   
    def condition(self, hand):
        self.penalties_and_conditions(hand)
        best_suit_option = None
        best_card_to_change = None
        best_impact = -float("inf")
        hand_total_power = sum(card.total_power for card in hand)
        self.card_reset(hand)
                
        for card in hand:
            for suit in ALL_SUITS:
                temp_hand = copy.deepcopy(hand)
                for temp_card in temp_hand:
                    """if temp_card.priority == #kajgod bude priority od doppelgangera:
                        temp_card.condition()"""                    
                    if temp_card.name != "Book of Changes":   
                        temp_card.suit = suit                    
                            
                        self.penalties_and_conditions(temp_hand)
                        new_total_power = sum(c.total_power for c in temp_hand)
                        impact = new_total_power - hand_total_power
                        
                        if impact > best_impact:
                            best_suit_option = suit
                            best_impact = impact
                            best_card_to_change = temp_card.name
                    self.card_reset(temp_hand)
                            
                       
                    
        for card in hand:
            if card.name == best_card_to_change:
                card.suit = best_suit_option
                print(f"CHANGED CARD == {best_card_to_change} and SUIT CHANGED {best_suit_option}")
        self.penalties_and_conditions(hand)                       
        
                