import turtle

okno = turtle.Screen()
tk = turtle.Turtle()
tk.speed(0)
tk.left(90)

def square(turtl, a):
    for _ in range(4):
        turtl.forward(a)
        turtl.left(90)


def rosettes(turtl, dl, a):
    turtl.forward(dl)
    square(turtl, a)
    turtl.backward(dl)

k = 15

for i in range(int(360/k)):
    tk.penup()
    tk.forward(20)
    tk.pendown()
    rosettes(tk, 100, 50)
    rosettes(tk, 60, 40)
    rosettes(tk, 40, 20)
    rosettes(tk, 25, 10)
    rosettes(tk, 15, 7)
    tk.penup()
    tk.backward(20)
    tk.right(k)


turtle.exitonclick()