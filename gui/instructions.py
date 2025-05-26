import customtkinter as ctk

class Instructions(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)       
        self.configure(fg_color="#4E342E")
        self.init_screen()
        
    def init_screen(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0) 
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)
        
        
        self.instruction_canvas = ctk.CTkCanvas(self, width=900, height=600, bg="#4E342E")
        self.instruction_canvas.grid(row=1, column=1, pady=5, padx=5)
        scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.instruction_canvas.yview)
        self.instruction_canvas.configure(yscrollcommand=scrollbar.set)        
        scrollbar.grid(row=1, column=2, sticky="ns")
        
        self.info_area = ctk.CTkFrame(self.instruction_canvas)
        self.instruction_canvas.create_window((0, 0), window=self.info_area, anchor="nw")
        
        self.info_lbl = ctk.CTkLabel(self.info_area, text="", fg_color="#2B2B2B", font=("Georgia", 16, "bold"), justify="left", text_color="orange")
        self.info_lbl.grid(row=0, column=0, padx=10, pady=10)
        
        self.back_to_menu_btn = ctk.CTkButton(self, text="Main Menu",
                                              fg_color="green", height=60,
                                              command=self.back_to_menu, font=("Georgia", 14, "bold"))
        self.back_to_menu_btn.grid(row=0, column=1, padx=5, pady=5)
        
        instruction_text = """
        Objective:
        
        
        Create the best-scoring hand of 7 cards by drawing and discarding strategically.

        The player with the highest total score wins.
        
        
        Each card includes:
        

            1. Name - Unique to each card.

            2. Suit - One of 11 types (Army, Leader, Wizard, Weapon, Artifact, Beast, Land, Weather, Flood, Flame, Wild).

            3. Base Strength - A number located on the top left corner of the card.

            4. Bonus/Penalty - Additional effects that raise or lower the score based on other cards. 
                   

        Gameplay:
        

            On your turn, draw one card: either the top card from the deck or a face-up card from the discard area.

            Then discard one card to the discard area.

            Cards in the discard area are always visible and spread out.
            

        End of Game:
        

            The game ends immediately when there are 10 cards in the discard area.

            The highest total score wins. In a tie, all tied players share victory.
        
        
        Card Effects:
        
        
        BONUS

            Positive effects.

        PENALTY

            Negative effects.

        BLANKS

            Some cards cause others to be "blanked" - meaning they lose their name, suit, strength and all the effects. 
            

        CLEARS

            Removes penalties from other cards. Clear effect happens before other effects.


        There are rare circumstances where a chain of cards will affect one another.

        In these cases, the order of execution is: Doppelganger, Mirage, Shapeshifter and then Book of Changes.

        After those cards resolve their effects, other card effects like CLEAR, BONUS or PENALTY are resolved.
        """
        
        self.info_lbl.configure(text=instruction_text)
        
        self.info_area.update_idletasks() 
        self.instruction_canvas.configure(scrollregion=self.instruction_canvas.bbox("all"))
        self.instruction_canvas.config(width=self.info_area.winfo_width())
        
        self.instruction_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.instruction_canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.instruction_canvas.bind_all("<Button-5>", self._on_mousewheel)
        
    def _on_mousewheel(self, event):
        if event.num == 4:
            self.instruction_canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.instruction_canvas.yview_scroll(1, "units")
        else:
            self.instruction_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def back_to_menu(self):
        self.destroy()