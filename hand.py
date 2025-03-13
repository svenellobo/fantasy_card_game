

class Hand():
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
            if card.has_clear == True:
                card.clear_penalties(hand)
            
        for card in hand:
            card.condition(hand)