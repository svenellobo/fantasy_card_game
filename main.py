import customtkinter as ctk
from gui.main_menu import MainMenu



class App(ctk.CTk):
    
    def __init__(self, title, geo):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")        
        self.geometry(geo)
        self.title(title)       
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #self.attributes("-fullscreen", True)
        screen_width = self.winfo_screenwidth() -35 
        screen_height = self.winfo_screenheight() -35
        self.geometry(f"{screen_width}x{screen_height}")
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
    
        self.main_menu = None
        self.initialize_main_menu()
        
        
        
    def initialize_main_menu(self):
        if not self.main_menu:  
            self.main_menu = MainMenu(self)
        else:             
            self.main_menu.grid()       
        
        

    
    
if __name__ == "__main__":
    app = App("Fantasy Realms", "1200x800")
    app.mainloop()   