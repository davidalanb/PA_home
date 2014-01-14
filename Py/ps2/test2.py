#import turtle

from myTurtle import *

wn = turtle.Screen()
mrb = turtle.Turtle()
mrb.speed(10)

draw_axes( wn, mrb )

mrb.pu()
mrb.forward(100)
mrb.right(90)
mrb.pd()

draw_square( wn, mrb, 50 )

mrb.pu()
mrb.left(180)
mrb.forward(300)
mrb.width(5)
mrb.color("blue")

draw_square( wn, mrb, 100 )

#myTurtle2.draw_axes( wn, mrb )

draw_star( mrb, 27, 200)

wn.mainloop()