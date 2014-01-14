import imp
import moreTurtle
imp.reload(moreTurtle)
from moreTurtle import *

def my_goto(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

wn = turtle.Screen()
wn.bgcolor('black')

mrb = turtle.Turtle()
mrb.speed(0)
mrb.color('red')
mrb.pensize(3)

my_goto(mrb,100,100)
draw_poly(mrb,8,50)

my_goto(mrb,250,100)
draw_poly(mrb,12,30)

draw_coords(mrb,[(100,-100),(150,-150),(200,-100)])

mrb.color('green')
my_goto(mrb, -300,300)
draw_chess( mrb, 4, 4, 50 )

my_goto(mrb,200,-100)
mrb.color('pink')
mrb.width(1)
draw_star(mrb, 17, 100)

wn.mainloop()