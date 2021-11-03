from tkinter import *
import tkinter.font as tkFont
import random


class Jeff():
    def __init__(self,x,y,imagename, canvas,name):
        self.x = x
        self.y = y
        self.xspeed = 2
        self.yspeed = 5
        self.name = name
        self.image = PhotoImage(file=imagename)
        # When we draw this image onto the canvas, it is assigned an ID number. We need to remember this
        # so that we can move the image later. We will store it within our Jeff object
        self.canvasID = canvas.create_image(self.x,self.y,image=self.image)

    def drag(self,canvas,x,y):
        self.x = x
        self.y = y
        canvas.coords(self.canvasID, self.x, self.y)
        
        
    def animate(self, canvas):
        self.x += self. xspeed
        self.y += self.yspeed

        if self.x > int(canvas.cget("width")) - self.image.width()//2:
            self.x = int(canvas.cget("width")) - self.image.width()//2
            self.xspeed *= -1
        if self.x <self.image.width()//2:
            self.x = self.image.width()//2
            self.xspeed *= -1

        if self.y > int(canvas.cget("height")) - self.image.height()//2:
            self.y = int(canvas.cget("height")) - self.image.height()//2
            self.yspeed *= -1
        if self.y <self.image.height()//2:
            self.y=self.image.height()//2
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
        self.b4 = Button(self, text= "Draggable", font=self.buttonfont, command= self.startDragging)
        self.b4.grid(row=4, column=1, sticky="EW")
        self.b5 = Button(self, text= "Mouse Points", font=self.buttonfont, command= self.startMousePoints)
        self.b5.grid(row=5, column=1, sticky="EW")
        self.theCanvas.bind("<B1-Motion>",self.drag)
        self.theCanvas.bind("<ButtonRelease-1>",self.dropped)
        self.theCanvas.bind("<Button-1>",self.clicked)    
        self.rowconfigure(6,weight=1)
        self.animating = False
        self.dragging = False
        self.myafterID=None
        self.mainloop()

    def gotfocus(self,e):
        self.texttest.delete(0,END)        

    def destroy(self):
        # All tkinter Widgets have a destroy() method which is used when you close the window
        # We are going to override it and provide our own version
        
        # We use 'after_cancel' to clean up the scheduled animation frame before the window closes down
        # Otherwise you get an error
        if self.myafterID:
            self.theCanvas.after_cancel(self.myafterID)
        # Now we can tell tkinter to finish off the rest of the normal Destroy command.
        super().destroy()  # super() refers to the parent class of this tkinter Widget. It is an example
                           # of polymorphism. We are altering the existing Destroy command of the parent.
        
        
    def drawShapes(self):
        self.points = False
        if self.dragging:
            self.startDragging()
        if self.animating:
            self.animate()
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
        self.points = False
        if self.dragging:
            self.startDragging()
        if self.animating:
            self.animate()
        self.theCanvas.delete(ALL)
        self.jeffpic = PhotoImage(file="jeff.png") # We can use PNGs but they need to be converted into a special format first
        for _ in range(5):
            # this procedure draws 5 images on the canvas, but forgets their positions so they can not be moved or edited later
            self.theCanvas.create_image(random.randint(0,500),random.randint(0,500),image=self.jeffpic, anchor=NW)
        
    def animate(self):
        self.points = False
        if not self.animating:
            if self.dragging:
                self.startDragging()
            self.theCanvas.delete(ALL)
            self.b3.configure(text="Stop")
            # Make a Jeff
            self.theJeff = Jeff(200,200,"jeff.png",self.theCanvas,0)
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
            self.theJeff.animate(self.theCanvas)
            # And we schedule another update in 20 ms
            self.myafterID = self.theCanvas.after(30, self.animFrame)
        
    def startDragging(self):
        self.points = False
        if not self.dragging:
            if self.animating:
                self.animate() # stops the animation if its still running
            self.theCanvas.delete(ALL)
            self.dragging = True
            self.b4.config(text="Stop")
            
            self.jeffs = {} # make a dictionary so we can access them by ID
            for i in range(2):
                newJeff = Jeff(50+i*300,300,"jeff" + str(i) + ".png",self.theCanvas,"Jeff number " + str(i))
                self.jeffs[newJeff.canvasID] = newJeff
        else:
            self.b4.config(text="Draggable")
            self.dragging = False
            self.jeffs= []
        
    def drag(self,e):
        mouseX = e.x
        mouseY = e.y
        if self.dragging:
            # get ID of nearest picture
            IDNum = self.theCanvas.find_closest(mouseX, mouseY)[0]
            self.theCanvas.tag_raise(IDNum)
            self.jeffs[IDNum].drag(self.theCanvas, mouseX,mouseY)
    
    def dropped(self,e):
        mouseX = e.x
        mouseY = e.y
        if self.dragging:
            # get ID of nearest picture
            IDNum = self.theCanvas.find_closest(mouseX, mouseY)[0]
            self.theCanvas.tag_raise(IDNum)
            print(self.jeffs[IDNum].name + " dropped at ",mouseX, mouseY)
            
    def startMousePoints(self):
        self.dragging=False
        self.animating = False
        self.points = True
        self.theCanvas.delete(ALL)
        self.theCanvas.create_text(300,300,text="Click anywhere to identify positions", fill="#000000")
    
    def clicked(self,e):
        if self.points:
            self.theCanvas.delete(ALL)
            self.theCanvas.create_text(300,300,text="Click anywhere to identify positions", fill="#000000")
            self.theCanvas.create_text(300,400,text="Clicked at " + str(e.x) + ":" + str(e.y), fill="#000000")


if __name__ == "__main__":
    app = App()
