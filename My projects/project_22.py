from turtle import *

speed("fastest")
tracer(0)

colors = ['Yellow', 'Green', 'Purple']
start = 1 / 3
stop = 3
i = 0

def circle(dl):
    begin_fill()
    fillcolor(colors[i])
    for _ in range(int(360)):
        forward(dl)
        right(1)
    end_fill()


while stop >= start:
    circle(stop)
    stop -= 1 / 3
    i += 1
    if i % 3 == 0:
        i = 0

exitonclick()



