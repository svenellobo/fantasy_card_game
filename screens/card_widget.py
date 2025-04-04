import customtkinter as ctk
from PIL import Image, ImageTk

class CardWidget(ctk.CTkFrame):
    def __init__(self, parent, card_image_path):
        super().__init__(parent, border_width=2, corner_radius=10)
        self.parent = parent
        self.card_image_path = card_image_path        
        
        self.normal_size = (150, 220)
        #self.hover_size = (160, 230)
        self.enlarged_size = (300, 450)
        
        self.configure(width=self.normal_size[0], height=self.normal_size[1])
        
        self.card_image = self.load_image(self.card_image_path, self.normal_size)
        self.card_label = ctk.CTkLabel(self, image=self.card_image, text="")
        self.card_label.grid(row=0, column=0, padx=5, pady=5)        
        
        
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.card_label.bind("<Enter>", self.on_hover)
        self.card_label.bind("<Leave>", self.on_leave)
        
        self.card_label.bind("<Button-3>", self.on_click)
        
        
    def load_image(self, image_path, size):        
        image = Image.open(image_path)
        return ctk.CTkImage(light_image=image, size=size)
    
        
    def on_hover(self, event):
        #self.configure(width=self.hover_size[0], height=self.hover_size[1], border_color="yellow")
        self.configure( border_color="yellow")
        #self.card_image = self.load_image(self.card_image_path, self.hover_size)
        #self.card_label.configure(image=self.card_image)
        
        
    def on_leave(self, event):
        #self.configure(width=self.normal_size[0], height=self.normal_size[1], border_color="black")
        self.configure(border_color="black")
        #self.card_image = self.load_image(self.card_image_path, self.normal_size)
        #self.card_label.configure(image=self.card_image)
        
    def on_click(self, event, is_open=False):
        if not is_open: 
            enlarged_window = ctk.CTkToplevel(self.parent)
            enlarged_window.geometry(f"{self.enlarged_size[0]}x{self.enlarged_size[1]}")            
            
            enlarged_image = self.load_image(self.card_image_path, self.enlarged_size)
            enlarged_label = ctk.CTkLabel(enlarged_window, image=enlarged_image, text="")
            
            enlarged_label.grid(row=0, column=0, padx=10, pady=10)
            is_open = True
        else:
            enlarged_window.bind("<Button-3>", lambda e: enlarged_window.destroy())
            is_open = False
