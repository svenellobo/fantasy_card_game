import customtkinter as ctk
from gui.card_widget import CardWidget
from PIL import Image
from deck import Deck
from player import Player
from gui.score_screen import ScoreScreen


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.game = game
        self.init_screen()
        
        
    def display_cards(self, hand, area):
        if area == "player_hand":
            frame = self.hand_frame
        elif area == "opponent_hand":
            frame = self.opponent_frame
        elif area == "discard_area":
            frame = self.discard_area
            
                
        for widget in frame.winfo_children():
            widget.destroy()
            
        row = 0
        col = 0
        for card in hand:            
            if frame == self.discard_area:
                card_widget = CardWidget(frame, card.image, card, click_action=lambda c=card: self.game.take_card_from_discard(c))
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")                
                if col == 4:
                    row = 1
                    col = -1
            elif frame == self.hand_frame:
                card_widget = CardWidget(frame, card.image, card, click_action=lambda c=card: self.game.discard_from_hand(c))
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                
            else:
                card_widget = CardWidget(frame, card.image, card)
                card_widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
    
        
        
    def init_screen(self):        
        
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)  
        self.columnconfigure(0, weight=0, minsize=150)
        self.columnconfigure(1, weight=0)
        
        
        
        
        #Deck of cards
        self.draw_deck_frame = ctk.CTkFrame(self)
        self.draw_deck_frame.grid(row=1, column=0, sticky="ew", padx=40, pady=40)
        
        self.draw_button = ctk.CTkButton(self.draw_deck_frame, fg_color="purple", text="Draw from deck", command=lambda: self.game.draw_from_deck())
        self.draw_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        draw_image = Image.open("images/card_back.jpeg")
        draw_image_tk = ctk.CTkImage(light_image=draw_image, size=(150, 220))
        
        self.end_turn_btn = ctk.CTkButton(self, fg_color="red", text="End Turn", height=60, command=lambda: self.game.end_turn())
        self.end_turn_btn.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        
        #hands and draw
        self.draw_deck = ctk.CTkLabel(self.draw_deck_frame, image=draw_image_tk, text="", height=220, width=150, fg_color="red")
        self.draw_deck.grid(row=1, column=0, padx=5, pady=5) 
        
        self.hand_frame = ctk.CTkFrame(self, height=220, fg_color="blue") 
        self.hand_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
        #self.hand_frame.grid_propagate(False)     
             
        self.opponent_frame = ctk.CTkFrame(self, height=240, fg_color="green") 
        self.opponent_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.opponent_frame.grid_propagate(False)  
        
        #discard area
        self.discard_area_border = ctk.CTkFrame(self, height=500, fg_color="gray") 
        self.discard_area_border.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        #self.discard_area_border.grid_propagate(False)
        
        self.discard_area = ctk.CTkFrame(self.discard_area_border, height=500, fg_color="gray") 
        self.discard_area.pack(fill="both", expand=True, padx=2, pady=2)
        self.discard_area.pack_propagate(False)
        self.discard_area.bind("<Enter>", self.on_discard_area_hover)
        self.discard_area.bind("<Leave>", self.on_discard_area_leave)
        
        self.status_area = ctk.CTkFrame(self, height=220)
        self.status_area.grid(row=2, column=0, sticky="ew", padx=10, pady=40)
        self.end_turn_btn = ctk.CTkButton(self.status_area, fg_color="red", state="disabled", text="End Turn", height=60, command=lambda: self.game.end_turn())
        self.end_turn_btn.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.status_area_lbl = ctk.CTkLabel(self.status_area, text="",  wraplength=200)
        self.status_area_lbl.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
  
    
    
    def on_discard_area_hover(self, event):        
        self.discard_area_border.configure(fg_color="yellow")

    def on_discard_area_leave(self, event):        
        self.discard_area_border.configure(fg_color="gray") 
        
    def on_right_click(self):
        pass
              
    def open_score_screen(self, player1_hand, player2_hand):
        self.destroy()        
        score_screen = ScoreScreen(self.parent, player1_hand, player2_hand)
        score_screen.grid(row=0, column=0, sticky="nsew")
        
            
        
    """def back_to_menu(self):        
        self.grid_forget()  
        self.parent.initialize_main_menu() """ 
        