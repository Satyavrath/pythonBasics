import numpy as np
import random

randomArray1 = np.random.random_sample((3,3))
print(randomArray1)
a, b = randomArray1.shape

columnList = [[randomArray1[row][column] for row in range(a)] for column in range(b) ]
print(columnList)