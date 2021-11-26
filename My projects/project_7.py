space = 15

def circle(n):
    print(space * " " + "#" * n)
    print((space - 1) * " " + "#" * (n+2))
    for i in range (n + 1):
        print((space - 2) * " " + "#" * (4 + n))
    print((space - 1) * " " + "#" * (n + 2))
    print(space * " " + "#" * n)



for i in range (6):
    if i % 2 != 0:
        circle(i + 2)
        space -= 1