from card import *

class GemOfOrder(Card):
    def __init__(self):
        super().__init__("Gem of Order", 5, ARTIFACT, 47)
        self.image = resource_path("images/gem_of_order.jpeg")
        self.save_original_state()
        
        
        
    @Card.not_blank   
    def bonus(self, hand):        
        base_powers = sorted({card.base_power for card in hand})
        max_run = 0
        current_run = 1
        
        for i in range(1, len(base_powers)):
            if base_powers[i] == base_powers[i-1] + 1:
                current_run += 1
                
                
            else:
                max_run = max(max_run, current_run)
                current_run = 1
                
        max_run = max(max_run, current_run)
        
        if max_run == 3:
            self.total_power += 10
        elif max_run == 4:
            self.total_power += 30
        elif max_run == 5:
            self.total_power += 60
        elif max_run == 6:
            self.total_power += 100
        elif max_run == 7:
            self.total_power += 150