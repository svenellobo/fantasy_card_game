import random

class Deck():
    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        pass

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def draw_card(self):
        if len(self.__cards) == 0:
            return
        return self.__cards.pop(0)