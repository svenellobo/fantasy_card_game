from hand import Hand

class CPUPlayer(Hand):
    def __init__(self):
          super().__init__()
              


def check_power(self, hand):
    lowest_power =  min(hand, key=lambda card: card.total_power)
    hand_total_power = sum(card.total_power for card in hand)
    for card in hand:
        #card.clear()
        #card.condition()
                