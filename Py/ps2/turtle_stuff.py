import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

'''
tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)
'''

alex = turtle.Turtle()       # Create alex

'''
tess.forward(80)             # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)               # Complete the triangle

tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin
'''
alex.pensize(5)
alex.color("orange")

from random import random

print( turtle.colormode())

wn.delay(3)

for x in range(0,30):
    r = random()*turtle.colormode()
    g = random()*turtle.colormode()
    b = random()*turtle.colormode()
    alex.color(r, g, b)
    alex.forward(300)
    alex.left(110)

'''
alex.forward(50)             # Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
'''

wn.mainloop()