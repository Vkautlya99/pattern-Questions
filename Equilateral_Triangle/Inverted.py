def Inverted_Equilateral_Triangle(row):
    for i in range(row, 0, -1):
       print(" " * (row - i) + "*" * (2 * i - 1))

row = 6
Inverted_Equilateral_Triangle(row)