from constants import *
import customtkinter as ctk
from PIL import Image


class Card():
    def __init__(self, name, power, suit, card_nmb):
        self.name = name
        self.base_power = power
        self.total_power = self.base_power
        self.suit = suit
        self.card_nmb = card_nmb    
        self.has_penalty = False
        self.has_clear = False
        self.is_blanked = False
        self.has_blank = False
        self.blanks_self=False
        self.priority = 5        
        self.image = None
        self.card_back_image = "images/card_back.jpeg"
        self.penalties_names = set()
        self.penalties_suits = set()  
        

    def __str__(self):
        return f"Card {self.card_nmb} {self.name} belongs to {self.suit} suit, has base power of {self.base_power} and total power of {self.total_power}" 
    
    def save_original_state(self):
        self.original_state = {
                "name": self.name,
                "base_power": self.base_power,
                "suit": self.suit,
                "card_nmb": self.card_nmb,
                "total_power": self.total_power,
                "has_penalty": self.has_penalty,
                "has_clear": self.has_clear,
                "is_blanked": self.is_blanked,
                "priority": self.priority,
                "penalties_names": self.penalties_names.copy(),
                "penalties_suits": self.penalties_suits.copy()
                
            }
    
    
    #decorator for checking if card is blanked
    @staticmethod
    def not_blank(func):
        def wrapper(self, *args, **kwargs):            
            if self.is_blanked:
                return 
            return func(self, *args, **kwargs)
        return wrapper

    def blank(self):
        self.name = None
        self.suit = None
        self.base_power = 0
        self.total_power = 0    
        self.has_penalty = False
        self.is_blanked = True
        
        
        
    
    def effect(self, hand):
        pass

    def clear_penalties(self, hand):
        pass
    
    @not_blank
    def activate_blank(self, hand):
        pass
    
    @not_blank
    def bonus(self, hand, discard_area=None):
        pass
    
    @not_blank
    def penalty(self, hand):
        pass

    
    
    def reset(self):        
        self.name = self.original_state["name"]
        self.base_power = self.original_state["base_power"]
        self.total_power = self.original_state["total_power"]
        self.suit = self.original_state["suit"]
        self.card_nmb = self.original_state["card_nmb"]        
        self.has_penalty = self.original_state["has_penalty"]
        self.is_blanked = self.original_state["is_blanked"]
        self.has_clear = self.original_state["has_clear"]
        self.penalties_suits = self.original_state["penalties_suits"]
        self.penalties_names = self.original_state["penalties_names"]

    