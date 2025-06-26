import customtkinter as ctk
from gui.main_menu import MainMenu
import ctypes
import platform



class App(ctk.CTk):
    
    def __init__(self, title):
        super().__init__()        
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green") 
        if platform.system() == "Windows":
            ctk.set_widget_scaling(0.8)
            self.state("zoomed")
        else:
            ctk.set_widget_scaling(1.0)
            try:
                self.attributes('-zoomed', True)
            except Exception:                
                screen_width = self.winfo_screenwidth() - 10
                screen_height = self.winfo_screenheight() - 50
                self.geometry(f"{screen_width}x{screen_height}+0+0")
                    
        self.title(title)       
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
    
        self.main_menu = None
        self.initialize_main_menu()
        
        
        
    def initialize_main_menu(self):
        if not self.main_menu:  
            self.main_menu = MainMenu(self)
        else:             
            self.main_menu.grid()       
        
        

    
    
if __name__ == "__main__":
    app = App("Fantasy Realms")
    app.mainloop()   