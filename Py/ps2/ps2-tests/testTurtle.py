import myTurtle

wn = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
myTurtle.draw_axes( wn, t )
t.speed(0)
myTurtle.draw_name( wn, t )
t.speed(0)
myTurtle.draw_line( wn, t, -3, 5 )

t.speed(0)
t.pu()
t.goto( 100, 100 )
t.pd()
myTurtle.draw_triangle( wn, t, 50 )

t.speed(0)
t.pu()
t.goto( 100, -100 )
t.pd()
myTurtle.draw_square( wn, t, 50 )

t.speed(0)
t.pu()
t.goto( -100, 100 )
t.pd()
myTurtle.draw_pent( wn, t, 50 )

turtle.mainloop()