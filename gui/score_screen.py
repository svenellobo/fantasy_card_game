import customtkinter as ctk
from gui.card_widget import CardWidget


class ScoreScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2):
        super().__init__(parent)        
        self.player1 = player1
        self.player2 = player2
        self.p1_score = self.player1.calculate_total_points()
        self.p2_score = self.player2.calculate_total_points()
        
              
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.init_screen()
        
        
    def init_screen(self):
        self.player_score_area = ctk.CTkFrame(self, fg_color="purple")
        self.player_score_area.grid(row=0, column=0, padx=5, pady=5)
        
        self.player_score_area.grid_columnconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(1, weight=1)
        
        
        self.player1_cards = ctk.CTkFrame(self.player_score_area, fg_color="green")
        self.player1_cards.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player1_cards.grid_columnconfigure(0, weight=1)
        self.player1_cards.grid_rowconfigure(0, weight=0)
        self.player1_cards.grid_rowconfigure(1, weight=1)        
        
        self.player1_score_lbl = ctk.CTkLabel(self.player1_cards, text=f"Player's hand and score: {self.p1_score}")
        self.player1_score_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=7, sticky="nsew")
         
        
        self.player2_cards = ctk.CTkFrame(self.player_score_area, fg_color="black")
        self.player2_cards.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player2_cards.grid_columnconfigure(0, weight=1)
        self.player2_cards.grid_rowconfigure(0, weight=1)
        self.player2_cards.grid_rowconfigure(1, weight=1)
        
        
        self.player2_score_lbl = ctk.CTkLabel(self.player2_cards, text=f"CPU's hand and score: {self.p2_score} ")
        self.player2_score_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=7, sticky="nsew") 
        
        
        p1_col = 0
        p2_col = 0
        for card in self.player1.cards_in_hand: 
            card_widget = CardWidget(self.player1_cards, card.image, card)
            card_widget.grid(row=1, column=p1_col, padx=5, pady=5, sticky="nsew")
            p1_col += 1
            
        for card in self.player2.cards_in_hand: 
            card_widget = CardWidget(self.player2_cards, card.image, card)
            card_widget.grid(row=1, column=p2_col, padx=5, pady=5, sticky="nsew")
            p2_col += 1
            
            
        
        
        close_button = ctk.CTkButton(self, text="Close Game", command=self.quit_game)
        close_button.grid(row=2, column=0, padx=10, pady=10)
        
        
    
                
            
        
    """def play_again(self):        
        self.destroy()
        from gui.game_screen import GameScreen
        GameScreen(self.master, game=self.master.create_game()).grid(row=0, column=0, sticky="nsew")"""

    def quit_game(self):
        self.quit()
    