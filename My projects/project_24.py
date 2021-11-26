def my_split(s, sep=' '):
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        wynik = my_split(s[pos+1:])
        wynik.insert(0, found)
        return wynik
    else:
        return [s]

print (my_split("Ala has a cat"))