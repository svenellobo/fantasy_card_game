from card import *
import copy

class BookOfChanges(Card):
    def __init__(self):
        super().__init__("Book of Changes", 3, ARTIFACT, 49)
        self.priority = 4
        self.image = "images/book_of_changes.jpeg"
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
            if card.priority == 5:
                card.bonus(hand)                
                card.penalty(hand)                
        
     
    @Card.not_blank   
    def bonus(self, hand):
        temp_hand = copy.deepcopy(hand) 
        mir = None                
        self.penalties_and_conditions(temp_hand)
        best_suit_option = None
        best_card_to_change = None
        best_impact = -float("inf")
        hand_total_power = sum(card.total_power for card in hand)
        self.card_reset(temp_hand)
        
                
        for temp_card in temp_hand:
            for suit in ALL_SUITS:
                """for card in hand:
                    if card.priority == 2:
                        mir = copy.deepcopy(card)"""               
                if temp_card.name != "Book of Changes":   
                    temp_card.suit = suit
                                            
                    self.penalties_and_conditions(temp_hand)
                    new_total_power = sum(c.total_power for c in temp_hand)
                    impact = new_total_power - hand_total_power
                    
                    if impact > best_impact:
                        best_suit_option = suit
                        best_impact = impact
                        best_card_to_change = temp_card.name
                """for card in temp_hand:
                    if card.priority == 2:
                        card = mir"""
                self.card_reset(temp_hand)
                            
                       
                    
        for card in hand:
            if card.name == best_card_to_change:
                card.suit = best_suit_option    
        
    """@Card.not_blank   
    def bonus(self, hand):
        self.card_reset(hand)
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
                card.suit = best_suit_option"""
                
                              
        
                