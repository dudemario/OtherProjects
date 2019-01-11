from turtle import *
from random import random
shape("turtle")

#Draws the circle in the background behind every H
def drawCircle(size):
    #return
    fill(True)
    right(90)
    forward(size/2)
    left(90)
    circle(size/2)
    left(90)
    forward(size/2)
    right(90)
    fill(False)

#Draws the main recursive pattern
def pat(size, depth, xfactor, yfactor):
    
    if depth!=0:        #Base Case: Exits if depth reaches the lowest level
        
        #Sets a random color for the drawings in the last two levels
        if depth <= 2:
            color((random(), random(), random()))

        #Calls the drawCircle function to draw circles
        drawCircle(size)

        #Loops twice to draw the lower half and then the higher half
        for i in xrange(2):
            right(90)
            forward(size/2.0*xfactor)
            right(90)
            forward(size*yfactor)
            pat(size/2, depth-1, xfactor, yfactor)  #Calls itself with a smaller size and a lower depth
            backward(size*yfactor)
            right(90)
            forward(size*xfactor)
            left(90)
            forward(size*yfactor)
            pat(size/2, depth-1, xfactor, yfactor)  #Calls itself again
            backward(size*yfactor)
            left(90)
            forward(size/2.0*xfactor)
            left(90)
            left(180)   #Turns around to draw the other (higher) side

        #Resets color to black for backwards movement
        color("white")

#Helper function to make the main code cleaner
def drawPat(size, n, xpos, ypos, xfactor, yfactor):
    bgcolor("black")    #Set background colors
    color("white")
    pu()
    screensize(size*xfactor*3.5, size*yfactor*3.5) #Set's screen size to fit the shape with extra room
    speed(0)            #Set as the fastest speed
    tracer(15)          #Increase speed even more
    setpos(xpos, ypos)  #Set pattern's origin position
    setheading(90)      #Set starting direction
    pd()
    pat(size, n, xfactor, yfactor)   #Start drawing
    pu()
    tracer(1)           #Reset tracer
    color(1,1,1)        #Reset color (white to stand out against black background)
    setpos(xpos, ypos)  #Reset position
    setheading(90)      #Reset direction
    pd()

#Main
drawPat(128, 5, 0, 0, 1.5, 0.5) #Change the 2nd number (depth) and see, anything above 7 is unreasonable
mainloop()
