from duze_cyfry import daj_cyfre
# generate all the numbers, save them in a list and then recall them
def number_in_hasz(number):
    list = []
    for i in range(len(number)):   #for the length of this string, it returns agrument, i.e. if I have 145, it adds 1, then 4 and 5 and creates a recipe for drawing
        list.append(daj_cyfre(int(number[i])))   #important to change to int, the expression fits in the string


    for i in range(5):   # or 5 instead of len (list [0]) the length of the list in the list, but it's always 5
        for j in range(len(list)):
            print(list[j][i], end=' ')  #draws the first line of each number and moves to a new line with print ()
        print()

number = input('Enter a number: ')
number_in_hasz(number)