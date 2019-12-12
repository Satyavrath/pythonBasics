
# to find the substring
'hello'[3]
#from zero to 3
'hello'[:2]

#syntax for substring
# "string"[start:end:increment]


# creating an array

newArray = ["Hello","d"]
newArray[1]
newArray[0][-1]
newArray[0][:-1]

data = "hey i bought | iphone| which is new"

reverse = data[-1::-1]
reverse
reverse = data[-1::-2]
reverse
# this three functions in the same way
data[data.index('|'):data.index('|',14)]
print(data[data.find('|')+1:data.find('|',14)])
data.split('|')
# this will split the data and assign to new varaiable in the form of array
newValue = data.split('|')
newValue
newValue[0]
newValue[1]

# this will split the data and assign to different variables
a,b,c = data.split('|')
a
b
c

# list which is similar to array 
# creates an empty list
list()
# list range of element range(start,end,step)
list(range(6))
list(range(0,5))




