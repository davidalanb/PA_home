#  These functions are the library!!!

def print_D( joe, color, width ):

    joe.color( color )
    joe.width( width )

    joe.pd()
    # D
    joe.circle(50,180)
    joe.left(90)
    joe.forward(100)

    # next
    joe.left(90)
    joe.penup()
    joe.forward(50)

def print_A( joe, color, width ):

    joe.color( color )
    joe.width( width )

    joe.pd()
    #A

    joe.pendown()
    joe.left(60)

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
    joe.left(180-30-90)
    joe.pu()
    joe.forward(20)

def print_V( joe, color, width ):

    joe.color( color )
    joe.width( width )
    joe.left(90)
    joe.pu()
    joe.forward(100)
    joe.pd()
    joe.right(180-30)
    joe.forward(100)
    joe.left(120)
    joe.forward(100)
    joe.pu()
    joe.right(150)
    joe.forward(100)
    joe.left(90)
    joe.forward(20)

# These two functions allow for entering a string,
# we'll expand the second to get each letter

def print_name( joe, name ):
    for l in name:
        print_letter( joe, l )

def print_letter( joe, l ):
    if ( l == 'D' ):
        print_D( joe, "red", 5 )
    elif( l == 'A' ):
        print_A( joe, "green", 5 )
    elif( l=='V' ):
        print_V( joe, "blue", 5 )

#------------------------ main -----------------------

'''
# setup
import turtle;
wn = turtle.Screen()
wn.screensize(800,600)
wn.bgcolor("black")
joe = turtle.Turtle()
joe.width( 5 )

# go to the left side of the screen
joe.pu()
joe.left(180)
joe.forward(400)
joe.left(180)

# Yay!
print_name( joe, "DAV" )
wn.mainloop()
'''