import customtkinter as ctk
from screens.card_widget import CardWidget
from PIL import Image
from deck import Deck
from player import Player


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.game = game
        self.init_screen()
        
        
    def display_cards(self, hand, player=True):
        frame = self.hand_frame if player else self.opponent_frame
                
        for widget in frame.winfo_children():
            widget.destroy()
        
        col = 0
        for card in hand:
            card_widget = CardWidget(frame, card.image)
            card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
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
        self.draw_button.grid(row=0, column=0, sticky="ew", padx=40, pady=40)
        draw_image = Image.open("images/card_back.jpeg")
        draw_image_tk = ctk.CTkImage(light_image=draw_image, size=(150, 220))
        
        #hands and draw
        self.draw_deck = ctk.CTkLabel(self.draw_deck_frame, image=draw_image_tk, text="", height=220, width=150, fg_color="red")
        self.draw_deck.grid(row=1, column=0, padx=5, pady=5) 
        
        self.hand_frame = ctk.CTkFrame(self, height=100, fg_color="blue") 
        self.hand_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10)     
             
        self.opponent_frame = ctk.CTkFrame(self, height=100, fg_color="green") 
        self.opponent_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)  
        
        #discard area
        self.discard_area_border = ctk.CTkFrame(self, height=500, fg_color="gray") 
        self.discard_area_border.grid(row=1, column=1, sticky="ew", padx=10, pady=10)        
        
        self.discard_area = ctk.CTkFrame(self.discard_area_border, height=500, fg_color="gray") 
        self.discard_area.pack(fill="both", expand=True, padx=2, pady=2)
        self.discard_area.bind("<Enter>", self.on_discard_area_hover)
        self.discard_area.bind("<Leave>", self.on_discard_area_leave)
        
        
        self.enlarged_card_display = ctk.CTkLabel(self.draw_deck_frame, image=None, text="", height=500, fg_color="gray")
        self.enlarged_card_display.grid(row=1, column=2, padx=10, pady=10)
        
              
        
 
    
    
    def on_discard_area_hover(self, event):        
        self.discard_area_border.configure(fg_color="yellow")

    def on_discard_area_leave(self, event):        
        self.discard_area_border.configure(fg_color="gray") 
        
    def on_right_click()
              
        
            
        
    """def back_to_menu(self):        
        self.grid_forget()  
        self.parent.initialize_main_menu() """ 
        