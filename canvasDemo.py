import tkinter as tk
from tkinter import font as tkFont
from winsound import *


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        self.title("Canvas Demo")
        
        lab1 = tk.Label(self, text="Canvas demo", font=self.titlefont)
        lab1.grid(row=0, column=0, sticky=tk.W)
        self.theCanvas =tk.Canvas(self, width=650,height = 600, bg="#fffed6")
        self.theCanvas.grid(row=1, column=0, rowspan=6)
        
        b1 = tk.Button(self, text= "Draw Shapes", font=self.buttonfont, command=self.drawShapes)
        b1.grid(row=1, column=1, sticky="EW")
        b2 = tk.Button(self, text= "Draw Pictures", font=self.buttonfont, command=self.drawImages)
        b2.grid(row=2, column=1, sticky="EW")
        b3 = tk.Button(self, text= "Animate", font=self.buttonfont)
        b3.grid(row=3, column=1, sticky="EW")
        
        self.rowconfigure(4,weight=1)
        
    def drawShapes(self):
        # this will clear the canvas and draw a series of shapes and text
        # the shape positions are not remembered, so it is not possible to erase or move them
        
        # The reference for these commands can be found at effbot.org/tkinterbook/canvas.htm
        
        self.theCanvas.create_rectangle(50, 50,300, 600, fill="white", outline="light green")
        self.theCanvas.create_oval(250, 50, 350, 500, fill="red")
        self.theCanvas.create_text(10,300,text="Sample text here", font=self.titlefont, anchor="w")
        
        # you can draw grids by using a loop
        
        #vertical lines
        for xpos in range(500,601,20):
            self.theCanvas.create_line(xpos,20,xpos,560) # left side of grid
        
        #horizontal lines
        for ypos in range(20,561,20):
            self.theCanvas.create_line(500,ypos, 600, ypos)
        
        
    def drawImages(self):
        self.theCanvas.delete(tk.ALL)
        jeffPic = tk.PhotoImage(file="sliderLeft.png")
        self.theCanvas.create_image(50, 50, image=jeffPic, anchor="nw")
        


window = App()