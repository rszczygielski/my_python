def chessboard (n, k):
    j = 1
    for i in range(n*2*k):       #important!!!! you have to multiply by k or else only half of the chessboard will be done
        if i % k == 0:         #allows you to change the position of the board, it happens as many times as a small square has the side length
            j *= -1
        if j < 0:                #and here, if it is negative, it displays continuously at the beginning
            print((" "*k+"*"*k)*n)
        elif j > 0:                #j positive it with a gap at the beginning
            print(("*"*k+" "*k)*n)


chessboard(4, 4)

