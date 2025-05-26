import customtkinter as ctk
from gui.card_widget import CardWidget
from PIL import Image, ImageTk


class ScoreScreen(ctk.CTkFrame):
    def __init__(self, parent, player1, player2, discard_area):
        super().__init__(parent) 
        self.player1 = player1        
        self.player2 = player2        
        self.player2.discard_area = discard_area.discard_area_cards                
        
        self.player1.penalties_and_conditions(self.player1.cards_in_hand)
        self.player2.penalties_and_conditions(self.player2.cards_in_hand)
        self.p1_score = self.player1.calculate_total_points()
        self.p2_score = self.player2.calculate_total_points()
        self.configure(fg_color="#4E342E")
        
        print("PLAYER 1 CARDS")
        for card in self.player1.cards_in_hand:            
            print(card)
            
        print("PLAYER 2 CARDS")    
        for card in self.player2.cards_in_hand:            
            print(card)
        
              
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)      
        
        self.init_screen()
        self.declare_winner()
        
    def init_screen(self):      
        
        self.player_score_area = ctk.CTkFrame(self, fg_color="#4E342E")
        self.player_score_area.grid(row=0, column=0, padx=5, pady=5) 

        self.winner_area = ctk.CTkFrame(self.player_score_area, fg_color="#2B2B2B")
        self.winner_area.grid(row=0, column=0, padx=5, pady=(5,35))
        
        self.winner_area.grid_rowconfigure(0, weight=1)
        self.winner_area.grid_columnconfigure(0, weight=1)
        
        self.winner_area_lbl = ctk.CTkLabel(self.winner_area, text="", anchor="center")
        self.winner_area_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=5, sticky="nsew")       
        
        
        self.player_score_area.grid_columnconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(0, weight=1)
        self.player_score_area.grid_rowconfigure(1, weight=1)
        
        
        self.player1_cards = ctk.CTkFrame(self.player_score_area, fg_color="#6D4C41")
        self.player1_cards.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player1_cards.grid_columnconfigure(0, weight=1)
        self.player1_cards.grid_rowconfigure(0, weight=0)
        self.player1_cards.grid_rowconfigure(1, weight=1)
        self.player1_cards.grid_rowconfigure(2, weight=1)        
        
        
            
        self.player1_score_lbl = ctk.CTkLabel(self.player1_cards,
                                              text=f"Player's hand and score: {self.p1_score}", font=("Georgia", 20, "bold"), fg_color="#2B2B2B", text_color="orange")
        self.player1_score_lbl.grid(row=0, column=0, padx=5, pady=5,  sticky="nsew", columnspan=len(self.player1.cards_in_hand))         
        
        
        self.player2_cards = ctk.CTkFrame(self.player_score_area, fg_color="#6D4C41")
        self.player2_cards.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        self.player2_cards.grid_columnconfigure(0, weight=1)
        self.player2_cards.grid_rowconfigure(0, weight=0)
        self.player2_cards.grid_rowconfigure(1, weight=1)
        self.player2_cards.grid_rowconfigure(2, weight=1)
        
        
        self.player2_score_lbl = ctk.CTkLabel(self.player2_cards,
                                              text=f"CPU's hand and score: {self.p2_score}", font=("Georgia", 20, "bold"),fg_color="#2B2B2B", text_color="orange")
        self.player2_score_lbl.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=len(self.player2.cards_in_hand)) 
        
        for col in range(7): 
            self.player1_cards.grid_columnconfigure(col, weight=1)
        for col in range(7):
            self.player2_cards.grid_columnconfigure(col, weight=1)
        
        
        p1_col = 0
        p2_col = 0
        for card in self.player1.cards_in_hand:
            point_difference = card.total_power - card.base_power
            if card.is_blanked:
                point_text = f"{'BLANKED'}"
                point_color = "orange"      
            elif point_difference < 0:
                point_text = f"-{abs(point_difference)}"
                point_color = "red"
            elif point_difference > 0:
                point_text = f"+{point_difference}"
                point_color = "#39FF14"
            elif point_difference == 0:    
                point_text = f"+{point_difference}"
                point_color = "white"
                
            suit_text = f"{card.suit} suit" if card.suit and card.suit != card.original_state["suit"] else ""
            text = (
                f"{point_text}\n"
                f"Total power: {card.total_power}\n"
                f"{card.name if card.suit and card.name != card.original_state['name'] else ''}\n"
                f"{suit_text}"
            )
            
            if card.is_blanked:                
                image = Image.open(card.image)
                grayscale_image = image.convert("L")                
                ctk_image = ctk.CTkImage(grayscale_image, size=(150, 220))
                
                card_widget = CardWidget(self.player1_cards, card.image, card)
                card_widget.grid(row=1, column=p1_col, padx=5, pady=5)
                card_widget.update_image(ctk_image)
                
                
                                
                card_info_area = ctk.CTkLabel(self.player1_cards,
                                               text=text,
                                               text_color=point_color,
                                               fg_color="#2B2B2B",
                                               font=("Georgia", 14, "bold"))
                card_info_area.grid(row=2, column=p1_col, padx=5, pady=5)                            
            
            else:
                
                card_widget = CardWidget(self.player1_cards, card.image, card)
                card_widget.grid(row=1, column=p1_col, padx=5, pady=5)
                
                card_info_area = ctk.CTkLabel(self.player1_cards,
                                               text=text,
                                               text_color=point_color,
                                               fg_color="#2B2B2B",
                                               font=("Georgia", 14, "bold"))
                card_info_area.grid(row=2, column=p1_col, padx=5, pady=5)               
            
            p1_col += 1
            
        for card in self.player2.cards_in_hand:
            point_difference = card.total_power - card.base_power      
            if card.is_blanked:
                point_text = f"{'BLANKED'}"
                point_color = "orange"       
            elif point_difference < 0:
                point_text = f"-{abs(point_difference)}"
                point_color = "red"
            elif point_difference > 0:
                point_text = f"+{point_difference}"
                point_color = "#39FF14"
            elif point_difference == 0:    
                point_text = f"+{point_difference}"
                point_color = "white"
                
            suit_text = f"{card.suit} suit" if card.suit and card.suit != card.original_state["suit"] else ""
            text = (
                f"{point_text}\n"
                f"Total power: {card.total_power}\n"
                f"{card.name if card.suit and card.name != card.original_state['name'] else ''}\n"
                f"{suit_text}"
            )
                
            if card.is_blanked:
                image = Image.open(card.image)
                grayscale_image = image.convert("L")                
                ctk_image = ctk.CTkImage(grayscale_image, size=(150, 220))
                
                card_widget = CardWidget(self.player2_cards, card.image, card)
                card_widget.grid(row=1, column=p2_col, padx=5, pady=5)
                card_widget.update_image(ctk_image)
                
                card_info_area = ctk.CTkLabel(self.player2_cards,
                                               text=text,
                                               text_color=point_color,
                                               fg_color="#2B2B2B",
                                               font=("Georgia", 14, "bold"))
                card_info_area.grid(row=2, column=p2_col, padx=5, pady=5)
            
            else:
                card_widget = CardWidget(self.player2_cards, card.image, card)
                card_widget.grid(row=1, column=p2_col, padx=5, pady=5)
                
                card_info_area = ctk.CTkLabel(self.player2_cards,
                                               text=text,
                                               text_color=point_color,
                                               fg_color="#2B2B2B",
                                               font=("Georgia", 14, "bold"))
                card_info_area.grid(row=2, column=p2_col, padx=5, pady=5) 
            p2_col += 1
            
            
        
        button_area = ctk.CTkFrame(self.player_score_area, fg_color="#6D4C41")
        button_area.grid(row=3, column=0, pady=10, padx=10)
        
        close_button = ctk.CTkButton(button_area, text="Close Game", font=("Georgia", 14, "bold"), command=self.quit_game, height=50, fg_color="#800000")
        close_button.grid(row=0, column=1, padx=10, pady=10)
        
        play_again_btn = ctk.CTkButton(button_area, text="Play Again", font=("Georgia", 14, "bold"), command=self.play_again, height=50, fg_color="green")
        play_again_btn.grid(row=0, column=0, padx=10, pady=10)
        
        
    def declare_winner(self):
        if self.p1_score > self.p2_score:
            self.winner_area_lbl.configure(text="Congratulations!!! You Win!!!", font=("Arial", 24, "bold"), text_color="#39FF14")
        
        elif self.p1_score < self.p2_score:
            self.winner_area_lbl.configure(text="You Lost! Better Luck Next Time!", font=("Arial", 24, "bold"), text_color="red")
            
        else:
            self.winner_area_lbl.configure(text="It's a Draw! Well Played!", font=("Arial", 24, "bold"), text_color="white")
            
                
            
        
    def play_again(self):
        self.destroy()

        from gui.game_screen import GameScreen
        from game import Game
        
        game_screen = GameScreen(self.master, None)
        new_game = Game(game_screen)
        game_screen.game = new_game       
        game_screen.grid(row=0, column=0, sticky="nsew")

    def quit_game(self):
        self.quit()
    