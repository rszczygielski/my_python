import turtle


okno = turtle.Screen()
tk = turtle.Turtle()
tk.speed(10)


def kwadrat(turtl, n):
    turtl.right(90)
    turtl.forward(n/2)
    for _ in range(3):
        turtl.left(90)
        turtl.forward(n)
    turtl.left(90)
    turtl.forward(n/2)
    turtl.left(90)

tk.hideturtle()
TK_DEFLUAT = tk.clone()

for _ in range(6):
    TK_DEFLUAT.setposition(0, 0)
    k = 60
    TK_DEFLUAT.right(60)
    tk = TK_DEFLUAT.clone()
    tk.penup()
    tk.forward(k-8)
    for _ in range(5):
        tk.pendown()
        kwadrat(tk, k)
        tk.penup()
        tk.forward(k)
        tk.pendown()
        k -= 10



turtle.exitonclick()