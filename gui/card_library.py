import customtkinter as ctk
from PIL import Image, ImageTk

class CardLibrary(ctk.CTkFrame):
    def __init__(self, parent, card_images):
        super().__init__(parent)
        self.images = card_images
        self.tk_images = []
        self.grid_rowconfigure(0, weight=1)       
        self.configure(fg_color="#4E342E")
        self.init_screen()

    
    def init_screen(self):
        self.card_library_canvas = ctk.CTkCanvas(self, width=900, height=600, bg="#4E342E")
        scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.card_library_canvas.yview)
        self.card_library_canvas.configure(yscrollcommand=scrollbar.set)
        self.card_library_canvas.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")        

        self.image_area = ctk.CTkFrame(self.card_library_canvas)
        self.card_library_canvas.create_window((0, 0), window=self.image_area, anchor="nw")
        
        self.card_library_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.card_library_canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.card_library_canvas.bind_all("<Button-5>", self._on_mousewheel)
        
        self.card_preview_frame = ctk.CTkFrame(self, fg_color="#4E342E")
        self.card_preview_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")
        
        self.card_preview_lbl = ctk.CTkLabel(self.card_preview_frame, text="Right click on a card to view it", fg_color="#4E342E", font=("Georgia", 14))
        self.card_preview_lbl.grid(row=1, column=0, padx=5, pady=5, sticky="ns")
        
        self.back_button = ctk.CTkButton(self.card_preview_frame, text="Back to Game", fg_color="green", height=60, command=self.back_to_game, font=("Georgia", 14, "bold"))
        self.back_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.grid_columnconfigure(2, weight=1)
        self.card_preview_frame.grid_rowconfigure(0, weight=0)
        self.card_preview_frame.grid_rowconfigure(1, weight=1)
        
        self.card_preview_frame.grid_columnconfigure(0, weight=1)

        row = 0
        column = 0
        for image_path in self.images:
            pil_image = Image.open(image_path)
            ctk_image = ctk.CTkImage(light_image=pil_image, size=(150, 220))
            self.tk_images.append(ctk_image)
            frame = ctk.CTkFrame(self.image_area, border_color="black", border_width=1, corner_radius=5)
            frame.grid(row=row, column=column, padx=5, pady=5)
            label = ctk.CTkLabel(frame, image=ctk_image, text="")
            label.grid(row=row, column=column, padx=5, pady=5)
            label.bind("<Enter>",  lambda event, frame=frame: self.on_hover(frame))
            label.bind("<Leave>", lambda event, frame=frame: self.on_leave(frame))
            label.bind("<Button-3>", lambda event, image=image_path: self.on_right_click(image, event))
            column += 1
            if column >= 5:
                column = 0
                row += 1

        self.image_area.update_idletasks()
        self.card_library_canvas.configure(scrollregion=self.card_library_canvas.bbox("all"))
        
    def _on_mousewheel(self, event):
        if event.num == 4:
            self.card_library_canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.card_library_canvas.yview_scroll(1, "units")
        else:
            self.card_library_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
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