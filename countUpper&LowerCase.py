userInput = input("Please enter a string")
UpperCaseCount = 0
LowerCaseCount = 0

for alphabet in userInput:
    if alphabet.isupper():
        UpperCaseCount+=1
    elif alphabet.islower():
        LowerCaseCount+=1
    else:
        pass

print("UpperCaseCount "+ str(UpperCaseCount))
print("LowerCaseCount "+ str(LowerCaseCount))
