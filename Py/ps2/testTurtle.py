import turtle
import myTurtle
import imp
imp.reload(myTurtle)    # makes sure you're working with the up-to-date version

wn = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
myTurtle.draw_axes( wn, t )

t.speed(0)
t.pu()
t.goto(0,0)
t.pd()
myTurtle.draw_name( wn, t )

t.speed(0)
myTurtle.draw_line( wn, t, -3, 5 )

t.speed(0)
t.pu()
t.goto( 200, 200 )
t.pd()
myTurtle.draw_triangle( wn, t, 50 )

t.speed(0)
t.width(1)
t.pu()
t.goto( 200, -200 )
myTurtle.draw_square( wn, t, 50 )
t.pd()
'''
r=255
g=0
b=0
for i in range(360//7*2):
    t.color((r/255,g/255,b/255))

    b+=255/(360/7)
    b%=255

    if ( i < (360/7)/2 ):
        g+=255/(360/7)
        g%=255
    else:
        g-=255/(360/7)
        g%=255

    r-=255/(360/7)
    r%=255

    t.right(7)
    myTurtle.draw_square( wn, t, 300 )

'''

t.speed(0)
t.pu()
t.goto( -200, 200 )
t.pd()
myTurtle.draw_pent( wn, t, 50 )

t.color('red')
t.width(2)
t.speed(3)
t.pu()
t.goto(-200,-200)
t.pd()
myTurtle.draw_star( t, 23, 125 )

turtle.mainloop()