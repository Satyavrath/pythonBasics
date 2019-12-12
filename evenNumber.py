

def evenNumber(number):
    return number%2 == 0


def test_even():
    assert evenNumber(2) == True
    assert evenNumber(3) == False
    assert evenNumber(5) == False
    assert evenNumber(8) == True
    print("The function is even")


test_even()


def oddNumber(number):
    return number%2 != 0


def test_odd():
    assert oddNumber(2) == False
    assert oddNumber(3) == True
    assert oddNumber(5) == True
    assert oddNumber(8) == False
    print("The function is odd")


test_odd()
    
