#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
middle = []
for row in matrix:
    middle.append(row[2:4])
print("Middle columns of the matrix are: {}".format(middle))
