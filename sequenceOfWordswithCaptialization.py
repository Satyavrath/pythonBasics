def caplitaze(*inputs):
    for word in inputs:
        a =  word.upper()
    return a
print(caplitaze("Hello world"))

# using lamda
# capitaliz = lambda *abc:  [x.upper() for x in abc]
# #
# print(capitaliz("Hello world","PRACTICE MAKES PERFECT"))
