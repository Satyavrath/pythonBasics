from math import *

def sqrtOfNumber(*input):
    C = 50
    H = 30
    result = []
    for i in input:
        Q = round(sqrt((2*C*i)/H))
        result.append(Q)
    return result


print(sqrtOfNumber(100,150,180))


