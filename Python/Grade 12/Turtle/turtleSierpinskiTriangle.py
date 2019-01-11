""" Draw a Sierpinski Triangle recursively

Aaron Quesnelle, April 2012

"""
from turtle import *
from random import random



def drawTriangle(p1, p2, p3):
    pencolor((random(), random(), random()))
    up()
    goto(p1)
    down()
    goto(p2)
    goto(p3)
    goto(p1)

def midPoint(p1, p2):
    return ((p1[0] + p2[0])/2.0, (p1[1]+p2[1])/2.0)

def sierpinski(p1, p2, p3, depth):

    if depth > 0:
        drawTriangle(p1, p2, p3)
        sierpinski(p1, midPoint(p1, p2), midPoint(p1, p3), depth-1)
        sierpinski(p2, midPoint(p2, p3), midPoint(p2, p1), depth-1)
        sierpinski(p3, midPoint(p3, p1), midPoint(p3, p2), depth-1)

    else:
        drawTriangle(p1, p2, p3)



speed(10)
pensize(1)

#when creating p1, p2 and p3 to use for original sierpinski call
#think about what data type they are.
sierpinski((200, 100), (0,0), (-200, 100), 5)


mainloop()
    



