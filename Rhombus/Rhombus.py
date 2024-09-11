def Rhombus(row) :
   for i in range(1, row + 1):
      print(" " * (row - i), end = "")
      print("*" * row)

row = 5
Rhombus(row)
