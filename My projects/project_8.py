def lucky_number(n):
    n = str(n)
    if ("777") in n:
        return True
    return False

def number_f(n):
    if n > 1:
        for i in range(2, n):   #tu może szukać też do n/2 żeby działał szybciej albo jeszcze szybciej dla n/2pierwiastka z 2, ponieważ
            if (n % i) == 0:
                return False
    return True

# wartość true jest czytelniejsza ponieważ nie wykożystuje tej liczby nigdzie dalej w kodzie jakbym dalej używał tej liczby to dałbym return

def number_f_l(n):
    if lucky_number(n) and number_f(n):
        return True

lista =[]

for i in range(1, 100000):
    if number_f_l(i):
        lista.append(i)
        print(i)


print(f'There is {len(lista)} those numbers')


