import turtle
import random
from turtle import *
# tracer(0)

speed("fastest")
wn = turtle.Screen()
def star(dl):
    fd(dl)
    r = random.randint(8, 13)      # r to ilość gałązek gwiazdki, jest losowana za każdym razem od 8 do 13
    for _ in range(r):
        fd(dl / 3)
        bk(dl / 3)
        rt(360 / r)






def rysunek(amount):
    for _ in range(amount):   # ilość jest to ilość patyczków gwiazdki, za każdym razem losowana jest inna długość nóżki od 200 do 320
        lg = random.randint(200,320)
        fd(lg)
        amount2 = random.randint(6,8)
        for _ in range(amount2):
            dl2 = random.randint(40,70)
            star(dl2)
            bk(dl2)
            rt(360/amount2)

        bk(lg)
        rt(360/amount)

rysunek(10)







exitonclick()



