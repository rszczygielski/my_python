from time import time
start = time()


def lucky_num(n, l_sied=3):
    n = str(n)
    if ("7" * l_sied) in n:
        print(n)
        return True
    return False


def f_number(n):
    n = int(n)
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    root = int(n**0.5) + 1
    for divider in range(3, root, 2):
        if n % divider == 0:
            return False
    return True


# generowanie liczb szczęśliwych
series3 = [str(x) for x in range(100, 1000)]
series2 = [str(x) for x in range(10, 100)]
series1 = [str(x) for x in range(10)]
list = []

for elem3 in series3:
    list.append(elem3 + "7" * 7)
    list.append('7' * 7 + elem3)

for elem2 in series2:
    for elem1 in series1:
        if elem1 != '0':
            list.append(elem1 + '7' * 7 + elem2)
        else:
            list.append('7' * 7 + elem1 + elem2)
        list.append(elem2 + '7' * 7 + elem1)


list.sort()
print(len(list))
list_f = []
for liczb in list:
    if f_number(liczb):
        list_f.append(liczb)
        print(liczb)

print(f'There is {len(list_f)} those numbers')
print(f'Program duration in seconds: {time() - start}')