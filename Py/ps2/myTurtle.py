
import turtle
import turtleName

#------------ function definitions

def draw_name( wn, guy ):
    turtleName.print_name( guy, "DAV" )

def draw_axes( wn, axes ):
    ( w, h ) = wn.screensize()      # get canvas width, height
    axes.penup()
    axes.goto(0,0)
    axes.pendown()
    axes.goto( -w,0 )
    axes.goto( w, 0)
    axes.goto(0,0)
    axes.goto(0,h)
    axes.goto(0,-h)
    axes.pu()

def draw_line(wn, guy, m,b):
    guy.pu()
    (w,h) = wn.screensize()
    x = -w
    y = m*x+b
    guy.goto(x,y)
    guy.pd()
    x = w
    y = m*x+b
    guy.goto(x,y)
    guy.pu()

def draw_poly(wn, guy, n, s):
    guy.pd()
    #angle=(n-2)*180/n
    angle=360/n
    for i in range(n):
        guy.left(angle)
        guy.forward(s)
    guy.pu()

def draw_triangle( wn,t,s):
    draw_poly(wn,t,3,s)

def draw_square( wn, t, s ):
    draw_poly(wn,t,4,s)

def draw_pent(wn, guy, s):
    draw_poly(wn,guy,5,s)

def draw_star( t, n, w ):
    t.pd()
    for i in range(n):
        t.forward(w)
        t.right(180-180/n)
    t.pu()

# ----------------- program main
'''
my_wn = turtle.Screen()
my_t = turtle.Turtle()
my_t.speed(0)

draw_axes( my_wn, my_t )
draw_line( my_wn, my_t, 3, -50 )

#my_t.fill(True)
my_t.color("red")
my_t.goto(0,0)
draw_poly( my_wn, my_t, 12, 75)
#my_t.fill(False)

my_t.pu()
my_t.goto( 100, 0 )
my_t.setheading(0)

my_t.color("orange")
my_t.write("asdf", font=("Arial", 24, "normal"))

my_t.right(90)
my_t.forward(100)

my_t.color("green")
draw_star( my_t, 11, 200)

my_t.right(90)
my_t.forward(300)
#draw_star( my_t, 27, 200)
my_t.color("blue")
draw_star(my_t, 111, 200)

my_wn.mainloop()
'''
