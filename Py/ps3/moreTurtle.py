import turtle
import math

def draw_poly(guy, n, s):
    guy.pd()
    #angle=(n-2)*180/n
    angle=360/n
    for i in range(n):
        guy.forward(s)
        guy.right(angle)
    guy.pu()

def draw_coords( t, list ):
    t.pu()
    t.goto(list[0])
    t.pd()
    for coord in list:
        t.goto( coord )


def draw_chess( t, rows, cols, w, h=None ):

    if not h:
        h=w

    t.seth(0)
    t.pd()

    for i in range(rows):

        for j in range(cols):
            t.right(90)
            t.forward(h)
            t.back(h)
            t.left(90)
            t.forward(w)

        t.right(90)
        t.forward(h)
        t.left(90)
        t.back( w*cols )

def draw_star( t, n, w ):
    t.pd()
    for i in range(n):
        t.forward(w)
        t.right(180-180/n)
    t.pu()

def draw_any_star( t, n, w ):
    t.pd()
    if( n < 3 ):
        return
    elif( n == 3 ):
        draw_poly( t, 3, w )
    elif( n == 4 ):
        draw_poly( t, 4, w )



    elif ( n%3 is 0):                   # multiples of 3 >=6
        r = (w/2)/math.cos( 30 * (math.pi/180) )
        for i in range( n//3 ):
            draw_poly(t,3,w)
            t.right(30)
            t.forward(r)
            if n>6:
                #t.right(180)
                t.right(180-360/n)
            t.forward(r)
            t.right(150)
            #t.right(180-360/n)
    elif( n% 4 is 0):                   # multiples of 4 >= 8
        r = (w/2)/math.cos( 45 * (math.pi/180) )
        for i in range( n//4 ):
            draw_poly(t,4,w)
            t.right(45)
            t.forward(r)
            t.right(180-360/n)
            t.forward(r)
            t.right(135)
    elif( n>=5 and n%2 is 1 ):           # odds >= 5
        draw_star(t, n, w)
    elif( n > 6 and n//2%2 is not 0 ):     # multiples of odds > 6
        draw_any_star( t, n//2, w)
        int_ang = 180/n
        t.right(int_ang)
        r = (w/2)/math.cos( int_ang/2 * (math.pi/180) )
        t.forward(2*r)
        t.right(180-int_ang)
        draw_any_star( t, n//2, w)
    t.pu()


def draw_mh_star(t, n, w):

    #find points on the circle

    return

#----------- testing

if __name__ == '__main__':

    wn = turtle.Screen()

    w, h = 800, 600
    wn.screensize(w, h)
    wn.bgcolor('black')

    mrb = turtle.Turtle()
    mrb.speed(0)
    mrb.color('green')
    mrb.pensize(1)

    draw_any_star(mrb, 1000, 100 )

    wn.mainloop()

def star_grid():
    wn = turtle.Screen()

    w, h = 800, 600
    wn.screensize(w, h)
    wn.bgcolor('black')

    mrb = turtle.Turtle()
    mrb.speed(0)
    mrb.color('blue')
    mrb.pensize(3)

    rows, cols = 4, 6
    col_w = w/cols
    col_h = h/rows

    mrb.pu()
    mrb.goto(-w/2, h/2)

    draw_chess( mrb, rows, cols, col_w, col_h )


    mrb.color('green')
    for i in range(rows):
        for j in range( cols ):

            x = -w/2 + j*col_w + col_w/2
            y = -h/2 + i*col_h + col_h/2

            mrb.pu()
            mrb.goto(x,y)
            mrb.speed(0)

            n = cols*i + j + 3
            draw_any_star( mrb, n, col_w/2 )

    wn.mainloop()
