def binaryc(inputs):
    binaryNumbers = inputs.split(",")
    a = []
    for i in binaryNumbers:
        if (int(i,2)%5 ==0):
            a.append(i)
    return ','.join(a)

print(binaryc("0100,0011,1010,1001,1111"))