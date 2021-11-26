from turtle import *
import random
import numpy as np

def sqare(b):

    for _ in range(4):
        fd(b)
        rt(90)

def line(b,il):

    for i in range (il):
        sqare(b)
        fd(b)
    rt(90)
    fd(b)


#line(50, 4)

def draw(b,n):
    speed("fastest")
    il = 1
    variable = 20
    begin_fill()
    fillcolor(np.array([1.0,1.0,0]))
    sqare(b)
    fd(b)
    end_fill()

    for i in range(n):
        for j in range(il):

            begin_fill()
            fillcolor(np.array([1.0 , 1 - i / (variable), i / (n - 1)]))
            sqare(b)
            fd(b)
            end_fill()
        rt(90)
        fd(b)
        il += 1


draw(20,18)


exitonclick()