import customtkinter as ctk
from PIL import Image, ImageTk

class CardLibrary(ctk.CTkFrame):
    def __init__(self, parent, card_images):
        super().__init__(parent)
        self.images = card_images
        self.tk_images = []
        self.init_screen()

    
    def init_screen(self):
        self.card_library_canvas = ctk.CTkCanvas(self, width=800, height=600)
        scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.card_library_canvas.yview)
        self.card_library_canvas(yscrollcommand=scrollbar.set)
        self.card_library_canvas.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.image_area = ctk.CTkFrame(self.card_library_canvas)
        self.image_area.create_window((0, 0), window=self.image_area, anchor="nw")

        row = 0
        column = 0
        for image_path in self.images:
            pil_image = Image.open(image_path)
            ctk_image = ctk.CTkImage(light_image=pil_image, size=(150, 220))
            self.tk_images.append(ctk_image)
            label = ctk.CTkLabel(self.image_area, image=ctk_image, text="")
            label.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column >= 5:
                column = 0
                row += 1

        self.image_area.update_idletasks()
        self.card_library_canvas.configure(scrollregion=self.card_library_canvas.bbox("all"))