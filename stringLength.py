def string_length(name):
    count = 0
    for string in name:
        count += 1
    return count


print(string_length("Hello"))

def test_stringLength():
    assert string_length("Hello") == 5
    assert string_length("myName") == 6
    print("The string works fine")
    


test_stringLength()


# last letter of string

def lastLetter(name):
    return name[-1]

print(lastLetter("Hdfasdfasdf"))
        
