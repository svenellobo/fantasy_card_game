from card import *
import copy

class Mirage(Card):
    def __init__(self):
        super().__init__("Mirage", 0, WILD, 52)
        self.save_original_state()
        self.mirage_suits = {ARMY: ["Knights", "Elven Archers", "Light Cavalry", "Dwarvish Infantry", "Rangers"],
                             LAND: ["Mountain", "Cavern", "Bell Tower", "Forest", "Earth Elemental"],
                             WEATHER: ["Rainstorm", "Blizzard", "Smoke", "Whirlwind", "Air Elemental"],
                             FLOOD: ["Fountain of Life", "Swamp", "Great Flood", "Island", "Water Elemental"],
                             FLAME: ["Wildfire", "Candle", "Forge", "Lightning", "Fire Elemental"]}
        
        
        
       
    def effect(self, hand):
        temp_hand = copy.deepcopy(hand)
        self.card_reset(temp_hand)        
        self.penalties_and_conditions(temp_hand)        
        best_impact = -float("inf")              
        hand_total_power = sum(card.total_power for card in temp_hand)
        self.card_reset(temp_hand)        
        
        