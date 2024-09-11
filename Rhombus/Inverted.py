def Inverted_Rhombus(row) :
   for i in range(row, 0, -1):

      print(" " * (row - i), end = "")
      print("*" * row)

row = 5
Inverted_Rhombus(row)
