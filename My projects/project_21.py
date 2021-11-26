from turtle import *
import random
import numpy as np
from duze_cyfry import daj_cyfre

penup()
fd(-300)
penup()
tracer(0)

def square(n=25, col=''):
    pendown()
    begin_fill()
    fillcolor(col)

    for i in range(4):
        forward(n)
        right(90)

    end_fill()
    penup()

def number_in_square(number):
    list = []
    for i in range(len(number)):
        list.append(daj_cyfre(int(number[i])))

    # print(list)
    # print(len(list))

    colors = [np.random.rand(3) for _ in range(len(list))]

    for i in range(5):
        for j in range(len(list)):
            for elem in list[j][i]:
                if elem == '#':
                    square(25,colors[j])
                forward(25)
            forward(25)
        right(90)
        forward(25)
        left(90)
        backward(25 * 5 * len(list) + 25 * len(list))




number = input('Enter a number: ')
number_in_square(number)

exitonclick()