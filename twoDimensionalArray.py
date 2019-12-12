from numpy import *

rowCount = int(input("Please enter number of rows"))
columnCount = int(input("Please enter number of columns"))
# to make a multi dimensional array
twodimensional = [[column for column in range(columnCount)] for row in range(rowCount)]
for i in range(rowCount):
    for j in range(columnCount):
       twodimensional[i][j] = (i*j)

print(twodimensional)