import numpy as np
input = np.array([[0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9,10, 11]
])
# print(len(input))
row, column = input.shape
def xValue(x):
    list = []
    for i in range(row):
        for j in range(column):
            if input[i][j] > 5:
                list.append(input[i][j])
    return list
print(xValue(input))
