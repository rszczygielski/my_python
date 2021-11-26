import turtle

okno = turtle.Screen()
tk = turtle.Turtle()
tk.speed(0)

for _ in range(9):
    for i in range(20, 40):
        tk.forward(i*5)
        tk.backward(i*5)
        tk.right(2)


turtle.exitonclick()