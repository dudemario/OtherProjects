from turtle import *
from random import randint
shape("turtle")
angle = 60
def koch(n, depth):
    global angle
    if depth == 1:
        forward(n)
        left(angle)
        forward(n*1.5)
        right(angle*2)
        forward(n*1.5)
        left(angle)
        forward(n)
    else:
        koch(n/4, depth-1)
        left(angle)
        koch(n/4, depth-1)
        right(angle*2)
        koch(n/4, depth-1)
        left(angle)
        koch(n/4, depth-1)


speed(0)
pensize(1)
def drawSnowflake(n, x, y):
    pu()
    setx(x-n/2.5)
    sety(y+n/4)
    pd()
    for i in xrange(3):
        koch(n, 4)
        right(120)
drawSnowflake(200, randint(-200, 200), randint(-200, 200))
mainloop()

