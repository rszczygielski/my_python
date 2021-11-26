import random

def randperm(n):
    list = []
    result = []
    duplicates = set()
    for i in range(0,n):
        list.append(i)

    while len(result) < n:
        p = random.choice(list)
        if p not in duplicates:
            result.append(p)
            duplicates.add(p)

    print(result)
    print(len(result))


randperm(10000)