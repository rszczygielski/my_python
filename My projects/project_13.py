from turtle import*
speed("slowest")
# tracer(0)


def tree(lg, lvl, angle):

    if lvl == 0:
        return

    fd(lg)
    rt(angle)
    tree(lg * 0.8, lvl-1,angle)
    lt(angle * 2)
    tree(lg * 0.8,lvl-1,angle)
    rt(angle)
    bk(lg)

left(90)
tree(100,8,20)

exitonclick()