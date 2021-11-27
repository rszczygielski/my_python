import math

def delta():

    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    a = int(a)
    b= int(b)
    c = int(c)

    delta = b**2 - 4*a*c

    if delta < 0:
        print("There is no solution")
    elif delta == 0:
        print("Only one solution", -b / (2*a))
    else: # delta > 0:
        print("Two solutiones")
        x1 = (-b - math.sqrt(delta) / (2 * a))
        x2 = (-b + math.sqrt(delta) / (2 * a))
        print(f'First root: x1={round(x1,3)}')
        print(f'Second root: x2={round(x2,3)}')


        vine_sum = x1 + x2
        vine_product = x1 * x2

        print(f'Vine product equals {round(vine_product,3)}\n',f'Vine sum equals {round(vine_sum,3)}')

delta()

