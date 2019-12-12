def multiInputs(a,b):
    list = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            list.append(a[i])
        if i < len(b):
            list.append(b[i])
    # if (len(a) != len(b)):
    #     c = len(b)-len(a)
    #     for i in range(len(a)):
    #         list.append(a[i])
    #         list.append(b[i])
    #     for j in range(c-1,-1,-1):
    #         list.append(b[len(b)-1-j])
    return list

a = [1,2,3,4]
b = ["a","b","c","d","e","f","g"]
# listA = [() for x,y in (a, b)]
# print("This is ", listA)
print(multiInputs(a,b))
