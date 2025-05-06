import customtkinter as ctk
from gui.card_widget import CardWidget
from PIL import Image, ImageTk


class ScoreScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2):
        super().__init__(parent)        
        self.player1 = player1
        self.player2 = player2
        self.player1.penalties_and_conditions(self.player1.cards_in_hand)
        self.player2.penalties_and_conditions(self.player2.cards_in_hand)
        self.p1_score = self.player1.calculate_total_points()
        self.p2_score = self.player2.calculate_total_points()
        self.configure(fg_color="#4E342E")
        
        for card in self.player1.cards_in_hand:
            print(card)
        
              
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)      
        
        self.init_screen()
        
        
    def init_screen(self):
        self.player_score_area = ctk.CTkFrame(self, fg_color="#4E342E")
        self.player_score_area.grid(row=0, column=0, padx=5, pady=5)
        
        self.player_score_area.grid_columnconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(1, weight=1)
        
        
        self.player1_cards = ctk.CTkFrame(self.player_score_area, fg_color="#6D4C41")
        self.player1_cards.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player1_cards.grid_columnconfigure(0, weight=1)
        self.player1_cards.grid_rowconfigure(0, weight=0)
        self.player1_cards.grid_rowconfigure(1, weight=1)
        self.player1_cards.grid_rowconfigure(2, weight=1)        
        
       
            
        self.player1_score_lbl = ctk.CTkLabel(self.player1_cards,
                                              text=f"Player's hand and score: {self.p1_score}")
        self.player1_score_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=len(self.player1.cards_in_hand), sticky="nsew")
         
        
        self.player2_cards = ctk.CTkFrame(self.player_score_area, fg_color="#6D4C41")
        self.player2_cards.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player2_cards.grid_columnconfigure(0, weight=1)
        self.player2_cards.grid_rowconfigure(0, weight=1)
        self.player2_cards.grid_rowconfigure(1, weight=1)
        self.player2_cards.grid_rowconfigure(2, weight=1)
        
        
        self.player2_score_lbl = ctk.CTkLabel(self.player2_cards,
                                              text=f"CPU's hand and score: {self.p2_score} ")
        self.player2_score_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=len(self.player2.cards_in_hand), sticky="nsew") 
        
        for col in range(7): 
            self.player1_cards.grid_columnconfigure(col, weight=1)
        for col in range(7):
            self.player2_cards.grid_columnconfigure(col, weight=1)
        
        
        p1_col = 0
        p2_col = 0
        for card in self.player1.cards_in_hand:
            point_difference = card.total_power - card.base_power
            if card.is_blanked:
                point_text = f"{"BLANKED"}"
                point_color = "black"       
            elif point_difference < 0:
                    point_text = f"-{abs(point_difference)}"
                    point_color = "red"
            elif point_difference > 0:
                point_text = f"+{point_difference}"
                point_color = "green"
            elif point_difference == 0:    
                point_text = f"+{point_difference}"
                point_color = "#B0B0B0"
            
            if card.is_blanked:                
                image = Image.open(card.image)
                grayscale_image = image.convert("L")                
                ctk_image = ctk.CTkImage(grayscale_image, size=(150, 220))
                
                card_widget = CardWidget(self.player1_cards, card.image, card)
                card_widget.grid(row=1, column=p1_col, padx=5, pady=5)
                card_widget.update_image(ctk_image)
                 
                card_info_area = ctk.CTkLabel(self.player1_cards,
                                               text=f"{point_text}\nTotal power: {card.total_power}\n{card.name if card.suit and card.name != card.original_state['name'] else ''}\n{card.suit if card.suit and card.suit != card.original_state['suit'] else ''}",
                                               text_color=point_color,
                                               fg_color="#5D4037")
                card_info_area.grid(row=2, column=p1_col, padx=5, pady=5)                            
            
            else:
                card_widget = CardWidget(self.player1_cards, card.image, card)
                card_widget.grid(row=1, column=p1_col, padx=5, pady=5)
                
                card_info_area = ctk.CTkLabel(self.player1_cards,
                                               text=f"{point_text}\nTotal power: {card.total_power}\n{card.name if card.suit and card.name != card.original_state['name'] else ''}\n{card.suit if card.suit and card.suit != card.original_state['suit'] else ''}",
                                               text_color=point_color,
                                               fg_color="#5D4037")
                card_info_area.grid(row=2, column=p1_col, padx=5, pady=5)               
            
            p1_col += 1
            
        for card in self.player2.cards_in_hand:
            point_difference = card.total_power - card.base_power      
            if card.is_blanked:
                point_text = f"{"BLANKED"}"
                point_color = "black"       
            elif point_difference < 0:
                    point_text = f"-{abs(point_difference)}"
                    point_color = "red"
            elif point_difference > 0:
                point_text = f"+{point_difference}"
                point_color = "green"
            elif point_difference == 0:    
                point_text = f"+{point_difference}"
                point_color = "#B0B0B0"
                
            if card.is_blanked:
                image = Image.open(card.image)
                grayscale_image = image.convert("L")                
                ctk_image = ctk.CTkImage(grayscale_image, size=(150, 220))
                
                card_widget = CardWidget(self.player2_cards, card.image, card)
                card_widget.grid(row=1, column=p2_col, padx=5, pady=5, sticky="nsew")
                card_widget.update_image(ctk_image)
                
                card_info_area = ctk.CTkLabel(self.player2_cards,
                                               text=f"{point_text}\nTotal power: {card.total_power}\n{card.name if card.suit and card.name != card.original_state['name'] else ''}\n{card.suit if card.suit and card.suit != card.original_state['suit'] else ''}",
                                               text_color=point_color,
                                               fg_color="#5D4037")
                card_info_area.grid(row=2, column=p2_col, padx=5, pady=5)
            
            else:
                card_widget = CardWidget(self.player2_cards, card.image, card)
                card_widget.grid(row=1, column=p2_col, padx=5, pady=5, sticky="nsew")
                
                card_info_area = ctk.CTkLabel(self.player2_cards,
                                               text=f"{point_text}\nTotal power: {card.total_power}\n{card.name if card.suit and card.name != card.original_state['name'] else ''}\n{card.suit if card.suit and card.suit != card.original_state['suit'] else ''}",
                                               text_color=point_color,
                                               fg_color="#5D4037")
                card_info_area.grid(row=2, column=p2_col, padx=5, pady=5) 
            p2_col += 1
            
            
        
        
        close_button = ctk.CTkButton(self, text="Close Game", command=self.quit_game)
        close_button.grid(row=2, column=0, padx=10, pady=10)
        
        
    
                
            
        
    """def play_again(self):        
        self.destroy()
        from gui.game_screen import GameScreen
        GameScreen(self.master, game=self.master.create_game()).grid(row=0, column=0, sticky="nsew")"""

    def quit_game(self):
        self.quit()
    