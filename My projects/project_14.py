from turtle import *

speed(0)
left(90)

i = 20
dod = 1
for _ in range(12):
    for _ in range(20, 35):
        if i > 27 or i < 20:
            dod *= -1
        forward(i*5)
        backward(i*5)
        right(2)
        i += dod


exitonclick()