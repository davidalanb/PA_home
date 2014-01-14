
# setup
import turtle;
wn = turtle.Screen()
joe = turtle.Turtle()
joe.width( 5 )

def print_letter( l ):
    if ( l == 'd' ):
        print_D()
    elif( l == 'a' ):
        print_A()
    elif( l=='v' ):
        print_V()

def print_D():
    joe.pd()
    joe.color("blue")
    # D
    joe.circle(50,180)
    joe.left(90)
    joe.forward(100)

    # next
    joe.left(90)
    joe.penup()
    joe.forward(50)
    joe.pendown()
    joe.left(60)

def print_A():
    joe.color("red")
    joe.pd()
    #A
    joe.forward(100)
    joe.right(180-60)
    joe.forward(50)
    joe.right(180-60)
    joe.forward(50)
    joe.right(180)
    joe.forward(50)
    joe.right(60)
    joe.forward(50)

    # next
    joe.left(180-30)
    joe.pu()
    joe.forward(100)
    joe.right(180-30)

def print_V():
    joe.color("green")
    joe.pd()
    joe.forward(100)
    joe.left(120)
    joe.forward(100)
    joe.pu()

def print_name( name ):
    for l in name:
        print_letter( l )

print_name( "dvadvdavdvvavd" )


wn.mainloop()