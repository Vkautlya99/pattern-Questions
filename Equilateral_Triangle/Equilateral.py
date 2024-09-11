# 3.Pyramid Star Pattern or Equilateral Triangle

def Equilateral_Triangle(row):
    for i in range(1, row + 1):

      print(" " * (row - i) + "*" * (2 * i - 1))
row = 6
Equilateral_Triangle(row)