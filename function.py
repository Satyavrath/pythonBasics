def product():
    a = 5
    b = 6
    c = a*b
    print(c)

product()


import turtle

myturtle = turtle.Turtle()

# defining a function with no argument
def square():
    myturtle.forward(50)
    myturtle.right(90)
    myturtle.forward(50)
    myturtle.right(90)
    myturtle.forward(50)
    myturtle.right(90)
    myturtle.forward(50)
    
square()

myturtle.forward(15)

# defining a function with two arguments

def square2(length,angle):
    myturtle.forward(length)
    myturtle.right(angle)
    myturtle.forward(length)
    myturtle.right(angle)
    myturtle.forward(length)
    myturtle.right(angle)
    myturtle.forward(length)
   

square2(60,90)

# for loop for repetative task

for i in range(4):
    square2(80,90)
        
    
