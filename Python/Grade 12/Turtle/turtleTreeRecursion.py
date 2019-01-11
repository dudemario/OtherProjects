"""Draw a tree recursively given a set depth.

Aaron Quesnelle, April 2012
"""
from turtle import *
from random import randint



def tree(trunkLength):
    if trunkLength < 5:
        return
    else:
        if trunkLength < 50:
            pencolor("green")
        else:
            pencolor("blue")
        turn = randint(10, 40)
        forward(trunkLength)
        left(turn)
        tree(trunkLength-randint(5, 25))
        right(turn*2)
        tree(trunkLength-randint(5, 25))
        left(turn)
        pu()
        backward(trunkLength)
        pd()
        
        
up()
shape("turtle")
setposition((0, -300))
setheading(90)
down()

speed(10)
pensize(3)

tree(100)

mainloop()
    



