from tkinter import *
import tkinter.font as tkFont
    

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        
        self.mainloop()
        

if __name__ == "__main__":
    app = App()
