from tkinter import *
import tkinter.font as tkFont
import tkinter.scrolledtext as scrolledtext
import random


class Jeff():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 2
        self.yspeed = 5
        self.image = PhotoImage(file="jeff.png")
        self.canvasID = None

        
    def move(self, canvas):
        self.x += self. xspeed
        self.y += self.yspeed

        if self.x > int(canvas.cget("width")) - self.image.width():
            self.x = int(canvas.cget("width")) - self.image.width()
            self.xspeed *= -1
        if self.x <0:
            self.x = 0
            self.xspeed *= -1

        if self.y > int(canvas.cget("height")) - self.image.height():
            self.y = int(canvas.cget("height")) - self.image.height()
            self.yspeed *= -1
        if self.y <0:
            self.y=0
            self.yspeed *= -1
        
        canvas.coords(self.canvasID, self.x, self.y)
        


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        
        lab1 = Label(self, text="Canvas demo", font=self.titlefont)
        lab1.grid(row=0, column=0, sticky=W)
        self.theCanvas =Canvas(self, width=650,height = 600, bg="#fffed6")
        self.theCanvas.grid(row=1, column=0, rowspan=6)
        
        self.b1 = Button(self, text= "Draw Shapes", font=self.buttonfont, command=self.drawShapes)
        self.b1.grid(row=1, column=1, sticky="EW")
        self.b2 = Button(self, text= "Draw Pictures", font=self.buttonfont, command=self.drawImages)
        self.b2.grid(row=2, column=1, sticky="EW")
        self.b3 = Button(self, text= "Animate", font=self.buttonfont, command= self.animate)
        self.b3.grid(row=3, column=1, sticky="EW")
        
        self.rowconfigure(4,weight=1)
        self.animating = False
    
    def destroy(self):
        # All tkinter Widgets have a destroy() method which is used when you close the window
        # We are going to override it and provide our own version
        
        # We use 'after_cancel' to clean up the scheduled animation frame before the window closes down
        # Otherwise you get an error
        self.theCanvas.after_cancel(self.myafterID)
        # Now we can tell tkinter to finish off the rest of the normal Destroy command.
        super().destroy()  # super() refers to the parent class of this tkinter Widget. It is an example
                           # of polymorphism. We are altering the existing Destroy command of the parent.
        
        
    def drawShapes(self):
        # this will clear the canvas and draw a series of shapes and text
        self.theCanvas.delete(ALL)
        # the shape positions are not remembered, so it is not possible to erase or move them
        
        # The reference for these commands can be found at effbot.org/tkinterbook/canvas.htm
        self.theCanvas.create_rectangle(50, 50,300, 600, fill="white", outline="light green")
        self.theCanvas.create_oval(250, 50, 350, 500, fill="red")
        self.theCanvas.create_text(10,300,text="Sample text here", font=self.titlefont, anchor="w")
        # The order matters. Images are drawn on top of each other
        
        # you can draw grids by using a loop
        #vertical lines
        for xpos in range(500,601,20):
            self.theCanvas.create_line(xpos,20,xpos,560) # left side of grid
        #horizontal lines
        for ypos in range(20,561,20):
            self.theCanvas.create_line(500,ypos, 600, ypos)
        
        
    def drawImages(self):
        self.theCanvas.delete(ALL)
        self.jeffpic = PhotoImage(file="jeff.png") # We can use PNGs but they need to be converted into a special format first
        for _ in range(5):
            # this procedure draws 5 images on the canvas, but forgets their positions so they can not be moved or edited later
            self.theCanvas.create_image(random.randint(0,500),random.randint(0,500),image=self.jeffpic, anchor=NW)
        
    def animate(self):
        if not self.animating:
            self.theCanvas.delete(ALL)
            self.b3.configure(text="Stop")
            # Make a Jeff
            self.theJeff = Jeff()
            # When we draw this image onto the canvas, it is assigned an ID number. We need to remember this
            # so that we can move the image later. We will store it within our Jeff object
            self.theJeff.canvasID = self.theCanvas.create_image(0,0,image=self.theJeff.image, anchor=NW)
            # We will use this boolean to keep track of whether we want our animation to continue, or to stop
            self.animating = True
            # We can't just use a loop here, because that would lock up the whole program
            # Instead, we schedule a frame update after a certain amount of time. In this case 5 milliseconds
            self.theCanvas.after(5, self.animFrame)
        else:
            self.animating = False
            self.b3.configure(text="Animate")
            
    
    def animFrame(self):
        # Assuming that we are still supposed to be animating...
        if self.animating:
            # We call the move function of our Jeff object. This handles the actual moving of the image on the
            # Canvas, so we send it the canvas as a parameter
            self.theJeff.move(self.theCanvas)
            # And we schedule another update in 20 ms
            self.myafterID = self.theCanvas.after(30, self.animFrame)
        


if __name__ == "__main__":
    app = App()
