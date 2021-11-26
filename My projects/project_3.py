def cross(n):
   k = " " * (n - 1)    # space in front of the vertical line of the cross
   for i in range(n):
      print(k, "*" * n)
   for i in range(n):
      print(("*" * n) * 3 )
   for i in range(n):
      print(k, "*" * n)           # same as first loop

cross(5)
