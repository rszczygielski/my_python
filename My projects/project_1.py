
def power(a ,n):
    result = 1
    for i in range(n):
        result *= a
    return result

def square(n):
    for i in range(n):
        for j in range(n):
            print ("*", end="")
        print()

def square2(n):
    for i in range(n):
        print (n * "#")



def square(n):
    for i in range(n):
        print("* " * n)

def square2(n):
    for i in range(n):
        print("#" * n)

def zadanie(k):
    ilosc = 0
    for i in range(5):
        print("Course", i)
        print("--" * 10)
        square(k + ilosc)
        ilosc += 2
        print()

    for i in range(5, 10):
        print("Course", i)
        print("--" * 10)
        square2(k + i - 5)
        print()

zadanie(3)


