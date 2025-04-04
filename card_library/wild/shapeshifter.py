from card import *
import copy

class Shapeshifter(Card):
    def __init__(self):
        super().__init__("Shapeshifter", 0, WILD, 51)
        self.priority = 3
        self.image = "images/shapeshifter.jpeg"
        self.save_original_state()        
        self.shape_suits = {ARTIFACT: ["Shield of Keth", "Gem of Order", "World Tree", "Book of Changes", "Protection Rune"],
                             LEADER: ["King", "Queen", "Princess", "Warlord", "Empress"],
                             WIZARD: ["Collector", "Enchantress", "Beastmaster", "Warlock Lord", "Necromancer"],
                             WEAPON: ["Warship", "Magic Wand", "Sword of Keth", "Elven Longbow", "War Dirigible"],
                             BEAST: ["Unicorn", "Basilisk", "Warhorse", "Dragon", "Hydra"]}
        
        
        
        
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
             
       
    def effect(self, hand):
        temp_hand = copy.deepcopy(hand)
        self.card_reset(temp_hand)        
        self.penalties_and_conditions(temp_hand)        
        best_impact = -float("inf")              
        hand_total_power = sum(card.total_power for card in temp_hand)
        best_suit = None
        best_name = None
        self.card_reset(temp_hand)
        
        
        for temp_card in temp_hand:
            if temp_card.original_state["name"] == "Shapeshifter":
                shape_card = temp_card
        
        for suit, names in self.shape_suits.items():
            for name in names:
                shape_card.name = name
                shape_card.suit = suit
                self.penalties_and_conditions(temp_hand)  
                new_total_power = sum(card.total_power for card in temp_hand)
                impact = new_total_power - hand_total_power
                
                if impact > best_impact:
                    best_impact = impact
                    best_suit = suit
                    best_name = name
                self.card_reset(temp_hand)
                        
        if best_suit and best_name:
            self.name = best_name
            self.suit = best_suit