import numpy as np
import random

val = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]

a = np.bincount(val)
print(a)
