def maxNumber(num1,num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "Both are equal"




def test_max():
    assert maxNumber(1,2)== 2
    assert maxNumber(3,2)== 3
    assert maxNumber('a','b')== 'b'
    print("works fine")

test_max()

#def bigNumber(num1,num2,num3):
#    if num1 > num2:
#        maxi = num1
#    else:
#        maxi = num2
#    if maxi > num3:
#        return maxi
#    else:
#        return num3



def bigNumber(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

def biggestNumber(num1,num2,num3):
    return bigNumber(bigNumber(num1,num2),num3)

def test_max():
    assert biggestNumber(1,2,3)== 3
    assert biggestNumber(3,4,2)== 4
    assert biggestNumber('a','b','c')== 'c'
    print("works fine")

test_max()

    
