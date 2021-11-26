def eryst(n):

    list = [x for x in range(2, n)]

    for i in list:
        for j in list:
            if i >= j:
                continue
            if j % i == 0:
                list.remove(j)
    return list


print(eryst(2130))