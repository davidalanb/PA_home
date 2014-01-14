

import math
import turtle

def draw_line(t, m, b):
    t.goto(0,b)
    t.pd()
    #if( m>0 ):
    t.setheading( math.atan(m) )
    #elif( m<0 ):
    #    t.setheading( math.pi - math.atan(-m) )
    #else:
    #    t.setheading(0)
    t.forward(500)
    t.back(1000)
    t.pu()

wn = turtle.Screen()
t = turtle.Turtle()
t.radians()
t.width(3)
t.color("red")
draw_line(t,3,5)
t.color("blue")
draw_line(t, -3, 5)

wn.mainloop()