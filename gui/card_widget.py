import customtkinter as ctk
from PIL import Image, ImageTk

class CardWidget(ctk.CTkFrame):
    def __init__(self, parent, card_image_path, card, click_action=None, right_click_action=None, drag_callback=None, interactive=False):
        super().__init__(parent, border_width=2, corner_radius=10)
        self.card_image_path = card_image_path 
        self.card = card
        self.click_action = click_action
        self.right_click_action = right_click_action
        self.drag_callback = drag_callback
        self.interactive = interactive
               
        
        self.normal_size = (150, 220)
        self.hover_size = (200, 270)
        self.enlarged_size = (300, 450)
        
        self.configure(width=self.normal_size[0], height=self.normal_size[1])
        
        self.card_image = self.load_image(self.card_image_path, self.normal_size)      
        
        
        self.card_label = ctk.CTkLabel(self, image=self.card_image, text="")        
        self.card_label.grid(row=0, column=0, padx=5, pady=5)
        self.card_label.bind("<Button-1>", self.on_left_click)
        self.bind("<Button-1>", self.on_left_click)        
        
        
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.card_label.bind("<Enter>", self.on_hover)
        self.card_label.bind("<Leave>", self.on_leave)        
        
        self.bind("<Button-1>", self.on_left_click)
        
        self.bind("<Button-3>", self.on_right_click)
        self.card_label.bind("<Button-3>",  self.on_right_click)
        
        #drag and drop        
        self.drag_data = {"x": 0, "y": 0, "widget": None}   
        
        if self.interactive == True:
            self.bind("<ButtonPress-1>", self.on_drag_start)
            self.bind("<B1-Motion>", self.on_drag_motion)
            self.bind("<ButtonRelease-1>", self.on_drag_stop)
            self.card_label.bind("<ButtonPress-1>", self.on_drag_start)
            self.card_label.bind("<B1-Motion>", self.on_drag_motion)
            self.card_label.bind("<ButtonRelease-1>", self.on_drag_stop)        
             
        
    def on_drag_start(self, event):        
        self.drag_data["widget"] = self
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.drag_data["start_x"] = self.winfo_x()
        self.drag_data["start_y"] = self.winfo_y()
        self.lift()

    def on_drag_motion(self, event):        
        x = self.winfo_x() - self.drag_data["x"] + event.x
        y = self.winfo_y() - self.drag_data["y"] + event.y
        self.place(x=x, y=y)

    def on_drag_stop(self, event):        
        dx = abs(self.winfo_x() - self.drag_data["start_x"])
        dy = abs(self.winfo_y() - self.drag_data["start_y"])
        if dx < 2 and dy < 2:            
            self.on_left_click(event)
        else:
            if self.drag_callback:
                self.drag_callback(self)
        self.drag_data["widget"] = None
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0
        
        
        
    def load_image(self, image_path, size):        
        image = Image.open(image_path)
        return ctk.CTkImage(light_image=image, size=size)
    
    def update_image(self, new_image):        
        self.card_label.configure(image=new_image)
    
    def on_left_click(self, event):
        if self.click_action:
            self.click_action(self.card)
            
    def on_right_click(self, event):
        if self.right_click_action:            
            self.right_click_action(self.card_image_path)
        
    def on_hover(self, event):        
        self.configure( border_color="yellow")        
        
        
    def on_leave(self, event):        
        self.configure(border_color="black")
        
    
