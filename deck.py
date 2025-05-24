import random
import os
import importlib, importlib.util
from utility import resource_path

class Deck():
    def __init__(self):
        self.cards = []
        self.image = resource_path("images/card_back.jpeg")
        self.create_deck()

    def create_deck(self):    
        self.cards = []
        card_dir = resource_path("card_library")

        for suit_folder in os.listdir(card_dir):
            suit_path = os.path.join(card_dir, suit_folder)

            if os.path.isdir(suit_path):
                for card_file in os.listdir(suit_path):
                    if card_file.endswith(".py") and card_file != "__init__.py":
                        card_file_name = card_file[:-3]
                        file_path = os.path.join(suit_path, card_file)
                        spec = importlib.util.spec_from_file_location(card_file_name, file_path)
                        card_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(card_module)
                        class_name = card_file_name.split("_")
                        class_name = "".join([part.capitalize() for part in class_name])
                        card_class = getattr(card_module, class_name)
                        
                        self.cards.append(card_class())  

        

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop(0)