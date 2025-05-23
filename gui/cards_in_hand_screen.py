
import customtkinter as ctk
from PIL import Image, ImageTk

class CardsInHandScreen(ctk.CTkFrame):
    def __init__(self, parent, hand_images):
        super().__init__(parent)
        self.hand_images = hand_images        
        self.tk_images = []               
        self.configure(fg_color="#4E342E")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.init_screen()        

    
    def init_screen(self):        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)  
        self.grid_rowconfigure(2, weight=1)  
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=0)  
        self.grid_columnconfigure(2, weight=1)
        
        center_frame = ctk.CTkFrame(self, fg_color="#4E342E")
        center_frame.grid(row=1, column=1)
        center_frame.grid_columnconfigure(0, weight=1)
        
        title_lbl = ctk.CTkLabel(center_frame, text="Cards in Hand:", font=("Georgia", 16, "bold"), text_color="orange", fg_color="#2B2B2B")
        title_lbl.grid(row=0, column=0, padx=5, pady=5, columnspan=10)
        
        hand_frame = ctk.CTkFrame(center_frame, fg_color="#6D4C41")
        hand_frame.grid(row=1, column=0, pady=5, padx=5)      
        
        
        
        
        col = 0
        for image_path in self.hand_images:
            pil_image = Image.open(image_path)
            ctk_image = ctk.CTkImage(light_image=pil_image, size=(150, 220))
            self.tk_images.append(ctk_image)            
            
            frame = ctk.CTkFrame(hand_frame, border_color="black", border_width=1, corner_radius=5)
            frame.grid(row=0, column=col, padx=5, pady=5)
            label = ctk.CTkLabel(frame, image=ctk_image, text="")
            label.grid(row=0, column=col, padx=5, pady=5)
            label.bind("<Enter>",  lambda event, frame=frame: self.on_hover(frame))
            label.bind("<Leave>", lambda event, frame=frame: self.on_leave(frame))
            label.bind("<Button-3>", lambda event, image=image_path: self.on_right_click(image, event))
            col += 1
            
        card_preview_frame = ctk.CTkFrame(center_frame, fg_color="#4E342E")
        card_preview_frame.grid(row=2, column=0, padx=10, pady=10)
        
        self.card_preview_lbl = ctk.CTkLabel(card_preview_frame, text="Right click on a card to view it",
                                             fg_color="#6D4C41", font=("Georgia", 14))
        self.card_preview_lbl.grid(row=0, column=0, padx=5, pady=5)
        
        self.back_button = ctk.CTkButton(self, text="Back to Choices",
                                         fg_color="green", height=60,
                                         command=self.back_to_game, font=("Georgia", 14, "bold"))
        self.back_button.grid(row=0, column=2, padx=5, pady=5)
            
        
        
    def back_to_game(self):
        self.grid_remove()
        
    def on_hover(self, frame):        
        frame.configure(border_color="yellow", border_width=2)
                
    def on_leave(self, frame):        
        frame.configure(border_color="black", border_width=1)
        
    def on_right_click(self, image, event):
        enlarged_image = Image.open(image) 
        resized_image = enlarged_image.resize((300, 450))  
        self.preview_ctk_image = ctk.CTkImage(resized_image, size=(300, 450))
        self.card_preview_lbl.configure(image=self.preview_ctk_image, text='')  
        self.card_preview_lbl.image = self.preview_ctk_image
        
    def back_to_game(self):
        self.grid_remove()
        
       