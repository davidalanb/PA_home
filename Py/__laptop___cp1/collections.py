my_tuple = ( 1, 2, "asdf", "etc.")

print( my_tuple[0] )

# TypeError
# my_tuple[0] = 5

my_list = [ 1, 2, "asdf", "etc."]

my_list[0] = 5

print( my_list)

my_tuple = my_list

print( my_tuple )


#### tuple packing / unpacking

address = ("5 Pinkterton St.", "Derry", "NH", "03038")
( street, city, state, zip ) = address

print( street )

test = [1,2,3,4]
[a,b,c,d] = test

print( test )

#### tuple return

import math

def quadratic(a, b, c):
    d = b**2 - 4*a*c       #discriminant
    x1 = (-1*b + math.sqrt(d)) / (2*a)
    x2 = (-1*b - math.sqrt(d)) / (2*a)
    return (x1, x2)

print( quadratic(1, 3, 2))

### iteration

shopping_list = ["bread", "eggs", "milk"]
for item in shopping_list:
    print(item)

### repetition

#print( "Hi\n"*7)
'''
for i in [0,1,2,3,4,5,6]:
    print( "Hi" )

for i in range(7):
    print( "Hi " + str(i) )

for i in range(0,7):
    print( "Hi " + str(i))

### turtle iteration
'''

print( list(range(1, 10, 2)) )


'''
import turtle
bob = turtle.Turtle()
wn = turtle.Screen()

for i in [0,1,2,3]:
    bob.forward(50)
    bob.left(90)

wn.mainloop()
'''



