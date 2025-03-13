import random

class Deck():
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        pass

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop(0)