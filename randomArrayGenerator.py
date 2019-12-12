import numpy as np
import random

# randomArray = np.random.rand(10,10)
# print(randomArray)
# print(randomArray.min())
# print(randomArray.max())

randomArray1 = np.random.random_sample((3,3))
print(randomArray1)
# print(randomArray1[0] ,randomArray1[1],randomArray1[2])
a, b = randomArray1.shape
# print(a)

columnList = [[randomArray1[row][y] for row in range(a)] for y in range(b) ]
print(columnList)