def Diamond_or_full_pyramid(row):
    for i in range(1, row+1):
       print(" " * (row - i) + "*" * (2 * i -1))
    for i in range(row, 0 ,-1):
       print(" " * (row - i) + "*" * (2 * i -1))



row = 6
Diamond_or_full_pyramid(row)       