
def squareNumber(number):
    return number**2

#print(squareNumber(4))


# wrting a test case to verify the answer.

def test_squareNumber():
    assert squareNumber(2) == 4
    assert squareNumber(4) == 16
    assert squareNumber(16) == 256
    #print("great job")


# calling a test function

test_squareNumber()
