import numpy as np
a = np.arange(11)
print(a)
listA = [-x for x in a if x>3 and x<=8]

print(listA)