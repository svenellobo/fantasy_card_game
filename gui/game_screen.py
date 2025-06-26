import customtkinter as ctk
from gui.card_widget import CardWidget
from PIL import Image
from gui.score_screen import ScoreScreen
from gui.player_choice_screen import PlayerChoiceScreen
from gui.card_library import CardLibrary
from gui.instructions import Instructions
from utility import resource_path


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.game = game
        self.library_open = False               
        self.configure(fg_color="#4E342E")
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
            
        
        disc_col = 1            
        row = 0
        col = 0
        for index, card in enumerate(hand):            
            if frame == self.discard_area:
                frame.grid_columnconfigure(0, weight=1) 
                frame.grid_columnconfigure(1, weight=0)  
                frame.grid_columnconfigure(2, weight=0)  
                frame.grid_columnconfigure(3, weight=0)  
                frame.grid_columnconfigure(4, weight=0)  
                frame.grid_columnconfigure(5, weight=0)
                frame.grid_columnconfigure(6, weight=1)
                
                card_widget = CardWidget(frame, card.image, card,
                                         click_action=lambda c=card: self.game.take_card_from_discard(c),
                                         right_click_action=lambda path=card.image: self.card_preview(path),
                                         )
                card_widget.grid(row=row, column=disc_col, padx=2, pady=5, sticky="nsew") 
                disc_col += 1               
                if disc_col == 6:
                    row += 1                    
                    disc_col = 1
                    
            elif frame == self.hand_frame:
                card_widget = CardWidget(frame, card.image, card,
                                         click_action=lambda c=card: self.game.discard_from_hand(c),
                                         right_click_action=lambda path=card.image: self.card_preview(path),
                                         drag_callback=self.reorder_cards,
                                         interactive=True)
                card_widget.grid(row=row, column=col, padx=2, pady=5, sticky="nsew")
                
            else:
                card_widget = CardWidget(frame, card.card_back_image, card)
                card_widget.grid(row=row, column=col, padx=2, pady=5, sticky="nsew")
            col += 1
            
    
        
        
    def init_screen(self): 
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=4)
        self.rowconfigure(2, weight=1)  
        self.columnconfigure(0, weight=0, minsize=150)
        self.columnconfigure(1, weight=0, minsize=1330)
        
               
        
        #Deck of cards
        self.draw_deck_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        self.draw_deck_frame.grid(row=1, column=0, sticky="ew", padx=40, pady=40)
        
        self.draw_button = ctk.CTkButton(self.draw_deck_frame, fg_color="green", state="normal",
                                         text="Draw from deck", font=("Verdana Arial", 14, "bold"), height=50, command=lambda: self.game.draw_from_deck())
        self.draw_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        #hands and draw
        draw_image = Image.open(resource_path("images/card_back.jpeg"))
        draw_image_tk = ctk.CTkImage(light_image=draw_image, size=(150, 220)) 
        self.draw_deck = ctk.CTkLabel(self.draw_deck_frame, image=draw_image_tk,
                                      text="", height=230, width=160)
        self.draw_deck.grid(row=1, column=0, padx=5, pady=5) 

        self.drag_hint = ctk.CTkFrame(self, height=220, fg_color="#2B2B2B") 
        self.drag_hint.grid(row=2, column=0, padx=10, pady=10)

        self.drag_hint_lbl = ctk.CTkLabel(self.drag_hint, font=("Verdana Arial", 14, "bold"),
                                           text_color="orange", text="You can rearrange the cards in your hand by clicking and dragging them.",  wraplength=200)            
        self.drag_hint_lbl.grid(row=0, column=0, padx=10, pady=10)

        
        self.hand_frame = ctk.CTkFrame(self, height=240, fg_color="#6D4C41", width=1320) 
        self.hand_frame.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
        self.hand_frame.grid_propagate(False)
             
             
        self.opponent_frame = ctk.CTkFrame(self, height=240, fg_color="#6D4C41") 
        self.opponent_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.opponent_frame.grid_propagate(False)  
        
        #discard area
        self.discard_area_border = ctk.CTkFrame(self, height=500, fg_color="#D7CCC8") 
        self.discard_area_border.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        self.discard_area_border.grid_propagate(False)
        
        
        self.discard_area = ctk.CTkFrame(self.discard_area_border, height=500, fg_color="#2E4F2E") 
        self.discard_area.pack(fill="both", expand=True, padx=2, pady=2)
        
        self.discard_area.grid_propagate(False)
        self.discard_area.bind("<Enter>", self.on_discard_area_hover)
        self.discard_area.bind("<Leave>", self.on_discard_area_leave)
        
        #end turn and menu area
        self.status_area = ctk.CTkFrame(self,  height=220, fg_color="#2B2B2B")
        self.status_area.grid(row=2, column=3, padx=10, pady=40)
        
        self.status_area.grid_rowconfigure(0, weight=1)
        self.status_area.grid_rowconfigure(1, weight=0)
        self.status_area.grid_rowconfigure(2, weight=1)
        self.status_area.grid_rowconfigure(3, weight=1)
        self.status_area.grid_columnconfigure(0, weight=1)
        self.status_area.grid_columnconfigure(1, weight=0)  
        self.status_area.grid_columnconfigure(2, weight=1)
        
        #right side buttons area
        self.end_turn_btn = ctk.CTkButton(self.status_area, fg_color="#800000", state="normal",
                                          text="End Turn", font=("Verdana Arial", 14, "bold"), height=60, command=lambda: self.game.end_turn())
        self.end_turn_btn.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
        
        self.status_area_lbl = ctk.CTkLabel(self.status_area, font=("Georgia", 14, "bold"), text="", text_color="orange",  wraplength=200)
        self.status_area_lbl.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        self.menu_area = ctk.CTkFrame(self,  height=220, fg_color="#2B2B2B")
        self.menu_area.grid(row=0, column=3, padx=10, pady=40)

        self.card_library_btn = ctk.CTkButton(self.menu_area, text="Card Library", font=("Verdana Arial", 14, "bold"), fg_color="green",height=60, command=lambda: self.open_card_library())
        self.card_library_btn.grid(row=0, column=0, padx=10, pady=10)

        self.instructions_button = ctk.CTkButton(self.menu_area, text="How to Play",
                                                  font=("Verdana Arial", 14, "bold"),
                                                  command=self.how_to_play,
                                                  height=60, fg_color="green")
        self.instructions_button.grid(row=1, column=0, padx=10, pady=10)

        #card preview area
        self.card_preview_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        self.card_preview_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.card_preview_frame.grid_rowconfigure(1, weight=1)
        self.card_preview_frame.grid_columnconfigure(0, weight=1)

        self.card_preview_info = ctk.CTkLabel(self.card_preview_frame, text="Right click on a card to view it",
                                              text_color="orange", font=("Verdana Arial", 16, "bold"), fg_color="#2B2B2B")
        self.card_preview_info.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        
        self.card_preview_lbl = ctk.CTkLabel(self.card_preview_frame, text="",
                                              text_color="orange", font=("Verdana Arial", 14, "bold"), height=220, width=150)        
        self.card_preview_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.rowconfigure(1, weight=4)
        self.columnconfigure(3, weight=1)
        
        
        
    
    
    def card_preview(self, image_path):        
        enlarged_image = Image.open(image_path) 
        resized_image = enlarged_image.resize((300, 450))  
        self.preview_ctk_image = ctk.CTkImage(resized_image, size=(300, 450))
        self.card_preview_lbl.configure(image=self.preview_ctk_image, text='')  
        self.card_preview_lbl.image = self.preview_ctk_image
        self.card_preview_info.configure(text="Right click on a card to view it")
        
    
    
    def on_discard_area_hover(self, event):        
        self.discard_area_border.configure(fg_color="yellow")
        
        
    def on_discard_area_leave(self, event):        
        self.discard_area_border.configure(fg_color="gray")         
    
              
    def open_score_screen(self, player1, player2, discard_area):
        self.destroy()        
        score_screen = ScoreScreen(self.parent, player1, player2, discard_area, self.game.image_paths)
        score_screen.grid(row=0, column=0, sticky="nsew")
        
    def open_choice_screen(self, player1, player2, discard_area):
        self.destroy()
        player_choice_screen = PlayerChoiceScreen(self.parent, player1, player2, discard_area, self.game.image_paths)
        player_choice_screen.grid(row=0, column=0, sticky="nsew")
        
    def reorder_cards(self, dragged_card_widget):
        widgets = sorted(
            self.hand_frame.winfo_children(),
            key=lambda widget: widget.winfo_x(),
        )
        self.game.player1.cards_in_hand = [widget.card for widget in widgets]
        
        for index, widget in enumerate(widgets):
            widget.grid(row=0, column=index, padx=5, pady=5, sticky="nsew")
        self.display_cards(self.game.player1.cards_in_hand, "player_hand")    
    
            
    def open_card_library(self):
        if not self.library_open:
            self.library_open = True
            self.card_library = CardLibrary(self.parent, self.game.image_paths)         
            self.card_library.grid(row=0, column=0, sticky="nsew")
        else:
            self.card_library.grid(row=0, column=0, sticky="nsew")

    def how_to_play(self):
        self.instruction = Instructions(self.parent)
        self.instruction.grid(row=0, column=0, sticky="nsew")

    def show_temporary_discard_message(self, message, duration=4000):        
        self.temp_discard_label = ctk.CTkLabel(
            self.discard_area,
            text=message,
            font=("Verdana Arial", 22, "bold"),
            text_color="orange",
            fg_color="transparent"
        )
        self.temp_discard_label.place(relx=0.5, rely=0.5, anchor="center")        
        self.after(duration, self.remove_temp_discard_label)

    def remove_temp_discard_label(self):
        if hasattr(self, "temp_discard_label") and self.temp_discard_label:
            self.temp_discard_label.destroy()
            self.temp_discard_label = None
        
        
   
        