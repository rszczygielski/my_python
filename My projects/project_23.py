import math
import statistics

def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1



def Collatza(n):
    result = []
    number = F(n)
    while 1 not in result:
        result.append(number)
        number = F(number)

    print(f"The energy of the number {n} is equal {len(result)}")
    print(result)
    print(f"Average energy of efficiency {statistics.mean(result)}")
    print(f"Median energy of efficiency {statistics.median(result)}")
    print(f"Maximum energy of excellence{max(result)}")
    print(f"Minimal energy of efficiency {min(result)}")



Collatza(7)


def analize_of_collatz(a,b):
    for i in range(a,b):
        print()
        print(f"Collins for {i} --------------------------------")
        Collatza(i)



analize_of_collatz(2,5)