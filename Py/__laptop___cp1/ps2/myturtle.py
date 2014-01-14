import sys
import turtle

global wn, height, width

def setup():
    global wn                   # use global, don't create local
    wn = turtle.Screen()
    wn.screensize(640,480)

    global width, height
    width=wn.screensize()[0]		# screensize returns an (x,y) pair
    height=wn.screensize()[1]

    wn.bgcolor("lightgreen")

def go_alex():
    # alex will draw the y-axis
    alex = turtle.Turtle()    # Create a turtle, assign to alex
    #alex.color("blue")
    alex.penup()
    alex.setpos(0,-1*height)
    alex.pendown()
    alex.goto(0,height)

def go_tess():
    # tess will draw the x-axis
    tess = turtle.Turtle()
    #tess.color("red")
    #tess.pensize(5)
    tess.penup()
    tess.goto(-1*width,0)
    tess.pendown()
    tess.goto(1*width,0)

# joe draws a line
def go_joe(m, b):
    x1 = -1*width
    y1 = m*x1 + b
    x2 = width
    y2 = m*x2 + b

    # joe will trace the line
    joe = turtle.Turtle()
    joe.color("orange")
    joe.pensize(2)
    joe.penup()
    joe.goto(x1, y1)
    joe.pendown()
    joe.goto(x2, y2)

# poly makes a polygon
def go_poly(n, s):
    poly = turtle.Turtle()
    poly.width(3)
    poly.color("purple")

    int_angle = (n-2)*180 / n

    for x in range(0,n):
        poly.forward(s)
        poly.right(180-int_angle)

    poly.hideturtle()

#--------------------

setup()
wn.delay(0)
go_alex()
go_tess()
wn.delay(10)
go_joe( 1/2, 60 )
#go_joe( 2, -60 )
go_poly( 5, 60)

# finish up
wn.mainloop()             # Wait for user to close window