import customtkinter as ctk

class CardWidget(ctk.CTkFrame):
    def __init__(self, parent, card_image):
        super().__init__(parent, border_width=2, corner_radius=10)
        self.parent = parent
        self.card_image = card_image        
        
        self.normal_size = (100, 150)
        self.hover_size = (110, 160)
        self.enlarged_size = (300, 450)
        
        self.configure(width=self.normal_size[0], height=self.normal_size[1])
        
        self.card_label = ctk.CTkLabel(self, image=card_image)
        self.card_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.card_label.bind("<Enter>", self.on_hover)
        self.card_label.bind("<Leave>", self.on_leave)
        
        self.card_label.bind("<Button-1>", self.on_click)
        
    def on_hover(self, event):
        self.configure(width=self.hover_size[0], height=self.hover_size[1], border_color="yellow")
    
    def on_leave(self, event):
        self.configure(width=self.normal_size[0], height=self.normal_size[1], border_color="black")
    
    def on_click(self, event):
        enlarged_window = ctk.CTkToplevel(self.parent)
        enlarged_window.geometry(f"{self.enlarged_size[0]}x{self.enlarged_size[1]}")
        #enlarged_window.title(self.card_name)
        
        enlarged_label = ctk.CTkLabel(enlarged_window, image=self.card_image)
        enlarged_label.grid(row=0, column=0, padx=10, pady=10)
        
        enlarged_window.bind("<Button-3>", lambda e: enlarged_window.destroy())
