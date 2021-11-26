from turtle import *
speed('fastest')
# tracer(0)

def side(lvl, dl):
    if lvl == 0:
        fd(dl)
    else:
        dl = dl / 3
        side(lvl-1, dl)
        fd(dl / 10)
        lt(90)
        side(lvl-1, dl)
        rt(90)
        side(lvl - 1, dl)
        rt(90)
        side(lvl - 1, dl)
        lt(90)
        fd(dl / 10)
        side(lvl - 1, dl)






def drawing(numer, dl):
    penup()
    goto(-200, 150)
    pendown()
    for _ in range(numer):
        side(numer,dl)
        rt(360/numer)



drawing(4,300)

exitonclick()