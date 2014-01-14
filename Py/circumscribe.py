


class Point:

    def __init__(self, x=0, y=0 ):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def dist_to_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def dist_to(self, p2):
        x1,y1=self.x, self.y
        x2,y2=p2.x, p2.y
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return d

    def slope_to_origin( self ):
        if self.x == 0:
            return None
        else:
            return self.y / self.x

    def slope_to(self, p2):
        x1,y1=self.x, self.y
        x2,y2=p2.x, p2.y

        if x1==x2:
            return None
        else:
            return (y2-y1)/(x2-x1)

    def stamp(self,t):
        t.pu()
        t.goto(self.x, self.y)
        t.stamp()


class Line:

    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

        self.slope = p1.slope_to(p2)
        self.y_int = None

        if self.slope is not None:
            self.y_int = p1.y - self.slope*p1.x

    def __str__(self):
        return "[{0}; {1}]".format(self.p1,self.p2)

    def to_str(self):
        return "[{0}; {1}]".format(self.p1,self.p2)

    def midpoint(self):
        return self.p1.halfway(self.p2)

    def perp_bis(self):

        p1 = self.p1.halfway( self.p2 )

        if self.slope:
            slope = -1/self.slope
            p2 = Point(p1.x+1, p1.y+slope)

        elif self.slope==0:
            slope = None
            p2 = Point(p1.x, p1.y+1)

        elif self.slope is None:
            slope = 0
            p2 = Point(p1.x+1, p1.y)

        return Line(p1,p2)

    def intersect( self, l2 ):

        if self.slope == l2.slope:
            return None

        elif self.slope==None:
            x = self.p1.x
            y = l2.slope*x + l2.y_int

        elif l2.slope == None:
            x = l2.p1.x
            y = self.slope*x + self.y_int

        else:
            a = self.slope
            b = self.y_int

            c = l2.slope
            d = l2.y_int

            x = (d - b) / (a - c)
            y = a*x + b

        return Point(x, y)

    def draw( self, t ):
        t.pu()
        t.goto(self.p1.x, self.p1.y)
        t.pd()
        t.goto(self.p2.x,self.p2.y)

class Triangle:

    def __init__( self, p1, p2, p3 ):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.cc = self.circumcenter()

    def circumcenter( self ):

        # for convenience
        p1, p2, p3 = self.p1, self.p2, self.p3

        # define and draw lines
        l1 = Line(p1,p2)
        l2 = Line(p2,p3)

        # get and stamp midpoints
        mid1_2 = l1.midpoint()
        mid2_3 = l2.midpoint()

        # find and draw perp. bisectors
        l3 = l1.perp_bis()
        l4 = l2.perp_bis()

        cc = l3.intersect(l4)
        return cc

    def draw( self, t, fill=False ):
        # for convenience
        p1, p2, p3 = self.p1, self.p2, self.p3

        if fill:
            t.begin_fill()

        Line(p1,p2).draw(t)
        Line(p2,p3).draw(t)
        Line(p3,p1).draw(t)

        t.end_fill()

    def circumscribe( self, t, fill=False ):

        t.pu()
        t.goto(self.cc.x,self.cc.y)
        #t.stamp()

        radius = self.cc.dist_to(self.p1)

        t.forward(radius)
        t.left(90)
        t.pd()

        if fill:
            t.begin_fill()

        t.circle(radius)
        t.end_fill()




import turtle
import random
import time

t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()

try:

    for i in range(3):
        w,h = s.screensize()

        pts={}

        for key in ['p1','p2','p3']:
            x = random.randint(-w,w)
            y = random.randint(-h,h)

            pts[key] = Point(x,y)

        '''
        # define points
        p1 = Point( -100, -200 )
        p2 = Point( -100, 200 )
        p3 = Point( 200, 200 )
        '''

        ta = Triangle(pts['p1'],pts['p2'],pts['p3'])

        t.color('red')
        ta.circumscribe(t, True)

        t.color('green')
        ta.draw(t, True)

        t.ht()

        time.sleep(1)

        t.clear()

    # end for
    #turtle.bye()
# end try


finally:
    #turtle.mainloop()
    turtle.bye()

#------------------------------------------------
'''
def distance( p1, p2 ):
    x1,y1=p1
    x2,y2=p2
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d

def draw_line(guy, line):
    m,b = line
    guy.pu()
    x = -1000
    y = m*x+b
    guy.goto(x,y)
    guy.pd()
    x = 1000
    y = m*x+b
    guy.goto(x,y)
    guy.pu()

def draw_seg(guy,p1, p2):
    guy.pu()
    guy.goto(p1)
    guy.pd()
    guy.goto(p2)


def line( p1, p2 ):
    x1, y1 = p1
    x2, y2 = p2

    m = (y2-y1)/(x2-x1)
    b = y1 - m*x1

    return (m, b)


def midpoint( p1, p2 ):
    x1, y1 = p1
    x2, y2 = p2
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return (mx, my)


def intersect( l1, l2 ):
    a, b = l1
    c, d = l2

    x = (d - b) / (a - c)
    y = a*x + b

    return (x, y)


def perp_bis( p1, p2 ):

    x1, y1 = p1
    x2, y2 = p2

    slope = (y2-y1)/(x2-x1)
    slope = -1/slope

    mx, my = midpoint( p1, p2 )
    b = my - slope*mx

    return ( slope, b )


def circumcenter( p1, p2, p3 ):

    # find two perpindicular bisectors
    l1 = perp_bis( p1, p2 )
    l2 = perp_bis( p2, p3 )

    # find intersection of them
    return intersect( l1, l2 )


p2 = ( 100, 200 )
p3 = ( -100, 300 )
p1 = ( 50, -200 )
cc = circumcenter( p1, p2, p3 )

radius = distance(cc,p1)


try:
    import turtle
    t = turtle.Turtle()
    s = turtle.Screen()
    t.speed(0)
    t.pu()
    for pt in [p1,p2,p3]:
        t.goto(pt)
        t.stamp()

    t.color('red')
    draw_line(t,line(p1,p2))
    draw_line(t,line(p2,p3))


    t.color('green')
    draw_line(t,perp_bis(p1,p2))
    draw_line(t,perp_bis(p2,p3))


    t.color('blue')
    t.goto(cc)
    t.stamp()

    t.forward(radius)
    t.left(90)
    t.pd()
    t.circle(radius)

finally:
    s.mainloop()
'''
