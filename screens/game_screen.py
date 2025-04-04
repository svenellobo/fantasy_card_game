import customtkinter as ctk
from screens.card_widget import CardWidget
from PIL import Image
from deck import Deck


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.selected_source = None
        #############################################################
        self.deck = Deck()
        ###############################################################
        self.init_screen()
        
        
    def display_cards(self, hand, player=True):
        if player:
            col = 0
            for card in hand:            
                card_widget = CardWidget(self.hand_frame, card.image)
                card_widget.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")            
                col += 1
        else:
            col = 0
            for card in hand:            
                card_widget = CardWidget(self.opponent_frame, card.card_back_image)
                #card_widget = CardWidget(self.opponent_frame, card.image)
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
        
        self.draw_button = ctk.CTkButton(self.draw_deck_frame, fg_color="purple", text="Draw from deck") #command=self.draw_button_click)
        self.draw_button.grid(row=0, column=0, sticky="ew", padx=40, pady=40)
        draw_image = Image.open("images/card_back.jpeg")
        draw_image_tk = ctk.CTkImage(light_image=draw_image, size=(150, 220))
        
        
        self.draw_deck = ctk.CTkLabel(self.draw_deck_frame, image=draw_image_tk, text="", height=220, width=150, fg_color="red")
        self.draw_deck.grid(row=1, column=0, padx=5, pady=5)      
             
        self.opponent_frame = ctk.CTkFrame(self, height=100, fg_color="green") 
        self.opponent_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)  
        
        self.discard_area = ctk.CTkFrame(self, height=500, fg_color="red") 
        self.discard_area.grid(row=1, column=1, sticky="ew", padx=10, pady=10) 
        
        self.hand_frame = ctk.CTkFrame(self, height=100, fg_color="blue") 
        self.hand_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10)      
        
 
    
    def on_discard_area_click(self, event):        
        self.player.choose_card_to_draw(self.deck, self.discard_area, source="discard")
        self.update_hand_display()
        
    """def draw_button_click(self):
            card = self.deck.draw_card()
            self.player.cards_in_hand.append(card)
            print(f"Card drawn from deck: {card.name}")
            #self.update_hand_display() """          
        
            
        
    def back_to_menu(self):        
        self.grid_forget()  
        self.parent.initialize_main_menu()  
        