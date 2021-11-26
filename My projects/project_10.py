def delete_bracket(nap):
    while "(" in nap and ")" in nap:
        for i in range(len(nap)):
            if nap[i] == "(":
                start = i
        for i in range(start, len(nap)):
            if nap[i] == ")":
                stop = i
                break
        nap = nap[:start] + nap[stop+1:]
    # nap = nap.split(" ")
    print(nap)
    # while "" in nap:
    #     nap.remove("")
    # return " ".join(nap)

delete_bracket("Ala has () a cat (and the cat) has something else) has an cat. ")
















