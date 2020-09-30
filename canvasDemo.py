from tkinter import *
import tkinter.font as tkFont
import tkinter.scrolledtext as scrolledtext
import random



class App:
    def __init__(self, master):
        self.master = master
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        
        lab1 = Label(master, text="Canvas demo", font=self.titlefont)
        lab1.grid(row=0, column=0, sticky=W)
        self.theCanvas =Canvas(master, width=650,height = 600, bg="#fffed6")
        self.theCanvas.grid(row=1, column=0, rowspan=6)
        
        b1 = Button(master, text= "Draw Shapes", font=self.buttonfont, command=self.drawShapes)
        b1.grid(row=1, column=1, sticky="EW")
        b2 = Button(master, text= "Draw Pictures", font=self.buttonfont, command=self.drawImages)
        b2.grid(row=2, column=1, sticky="EW")
        b3 = Button(master, text= "Animate", font=self.buttonfont)
        b3.grid(row=3, column=1, sticky="EW")
        
        master.rowconfigure(4,weight=1)
        
        
    def drawShapes(self):
        # this will clear the canvas and draw a series of shapes and text
        self.theCanvas.delete(ALL)
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
        self.theCanvas.delete(ALL)
        self.jeff = PhotoImage(file="jeff.png")
        for _ in range(5):
            self.theCanvas.create_image(random.randint(0,500),random.randint(0,500),image=self.jeff, anchor=NW)
        


if __name__ == "__main__":
    root = Tk()
    root.title("Canvas Demo")
    root.resizable(width=False, height=False)
    app = App(root)
    root.mainloop()
