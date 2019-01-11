"""Turtle draw a series of recursive squares.

Aaron Quesnelle, April 2012

"""
from turtle import *
shape("turtle")
def drawSquare(side):
    for i in range(0, 4):
        forward(side)
        right(90)


def nestedBox(side):
    if side >= 1:
        nestedBox(side-5)
        drawSquare(side)
    else:
        pass

def drawCentredSquare(x, y, side):
    pu()
    setx(x+side/2)
    sety(y+side/2)
    setheading(180)
    pd()
    for i in xrange(0, 4):
        forward(side)
        left(90)
def concentricSquares(x, y, side):
    if side < 1:
        pass
    else:
        drawCentredSquare(x,y, side)
        concentricSquares(x, y, side-6)
'''
speed(10)
pensize(3)
#call nestedBox here
nestedBox(50)
'''

speed(10)
pensize(1)
concentricSquares(0, 0, 100)

mainloop()



