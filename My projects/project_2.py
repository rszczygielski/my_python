list = []
list2= []


def silnia():
    result = 1
    number = 101
    for i in range(1, number + 1):
       result *= i
       list.append(result)



    for i in list:
        count = 0
        while i > 0:
            i = i // 10
            count = count + 1
        list2.append(count)



# def rozwiązanie(n):
#    ilość = 0
#    while ilość < n:
#       print("{}! have {} digits".format(ilość, list2[ilość]))
#       ilość += 1
#       if ilość == n:
#          break



############## LEPSZY SPOSÓB   trzeba zmienic formy gramatyczne
def strong(n):       #  funkction counts strong of a number
    if n < 1:
        return 1
    return n * strong(n - 1)


def cond_task(lb):       #funkcja z warunku zadania czyli wyświetla liczbe oraz dlusc ciagu znakow silni tej liczby
    lista = [2,3,4]
    list2 = [12,13,14]
    a = len(str(strong((lb)))) % 10
    if a in lista and len(str(strong((lb)))) not in list2:
        return (f'{lb}! ma {len(str(strong((lb))))} cyfry')     #important to change into len
    else:
        return (f'{lb}! ma {len(str(strong((lb))))} cyfr')


for i in range(4, 101):
    print(cond_task(i))







