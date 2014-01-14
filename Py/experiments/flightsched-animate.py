
class airport:

    def __init__( self, aps, name ):
        self.name=name
        aps.add( self )

class airports:

    def __init__( self ):
        self.airports=[]

    def add(self, ap ):
        self.airports.append( ap )

class flight:

    def __init__( self, fls, src, dest, d, cost=999 ):
        self.src = src
        self.dest = dest
        self.d = d
        self.cost = cost

        fls.add( [self] )

    def print(self):
        print( self.src.name, 'to', self.dest.name, self.d, 'miles' )


class flights:

    def __init__( self, fls=[] ):
        self.fls=[]
        for fl in fls:
            self.fls.append(fl)

    def add( self, fls ):
        for fl in fls:
            self.fls.append(fl)

    def print(self ):
        for fl in self.fls:
            fl.print()

    # return a list of paths,
    # path is a series of flights
    def route(self, src, dest):

        paths=[]        # successful
        data=[]        # stores data

        maybe=[]        # possible
        rest=[]         # leftover

        # first pass
        for fl in self.fls:
            if fl.src == src:
                if fl.dest == dest:
                    paths.append([fl])
                else:
                    maybe.append([fl])
            else:
                rest.append(fl)

        for route in maybe:
            self.route_r( paths, route, rest, dest )

        return paths

    def route_r(self, paths, route, rest, dest ):

        loc_maybe=[]

        fl = route[-1]
        loc_rest=[]

        for fl2 in rest:
            if fl.dest == fl2.src:
                if fl2.dest == dest:
                    loc_route = route[:]
                    loc_route.append(fl2)
                    paths.append(loc_route)
                else:
                    loc_route = route[:]
                    loc_route.append(fl2)
                    loc_maybe.append(loc_route)

            else:
                loc_rest.append(fl2)

        for route in loc_maybe:
            self.route_r( paths, route, loc_rest, dest )

def print_routes( rts ):
    for i, rt in enumerate(rts):
        print( "\tRoute",i+1 )
        dist=0
        for fl in rt:
            print('\t\t', end='')
            dist+=fl.d
            fl.print()
        print('\t\t---> Total distance:', dist, 'miles')

def least_route( rts ):
    if not rts:
        return
    least_dist = None
    ix = None
    for i, rt in enumerate(rts):
        dist=0
        for fl in rt:
            dist+=fl.d
        if least_dist is None or dist < least_dist: # short-circuit
            least_dist = dist
            ix=i

    return rts[ix], least_dist

def greatest_route( rts ):
    if not rts:
        return
    gr_dist = None
    ix = None
    for i, rt in enumerate(rts):
        dist=0
        for fl in rt:
            dist+=fl.d
        if gr_dist is None or dist > gr_dist: # short-circuit
            gr_dist = dist
            ix=i

    return rts[ix], gr_dist

def traveling_salesman( aps, rts ):
    if not rts:
        return
    least_dist=None
    ix=None
    for i, rt in enumerate(rts):
        if len(rt) < len(aps.airports):
            continue
        dist=0
        for fl in rt:
            dist+=fl.d
        if not least_dist:
            least_dist = dist
            ix=i
        elif dist < least_dist:
            least_dist = dist
            ix=i
    return rts[ix]

def dist(p1,p2):
    import math
    x1,y1 = p1
    x2,y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def draw_route(t, rt, data_pts, rgb, offset):

    from random import random
    t.width(3)
    t.color(rgb)
    t.speed(0)
    t.pu()
    x, y = data_pts[rt[0].src.name]
    x += offset
    y += offset

    t.goto( x,y )
    t.pd()
    for fl in rt:
        #could calculate slope to do offset right
        x, y = data_pts[fl.dest.name]
        x += offset
        y += offset
        t.goto( x,y )


def main():
    import turtle
    #import random
    from random import random, randint

    s = turtle.Screen()
    w,h = 800,600
    s.screensize(w,h)
    t = turtle.Turtle()
    t.speed(0)
    t.seth(90)

    # draw border
    t.pu()
    t.goto(-w/2, h/2)
    t.pd()
    t.goto(w/2, h/2)
    t.goto(w/2,-h/2)
    t.goto(-w/2,-h/2)
    t.goto(-w/2,h/2)
    t.pu()

    # number of cities
    aps = airports()
    my_aps={}
    data_pts={}
    n = 10

    s_char=65

    for i in range(n):
        name=chr(s_char+i)
        my_aps[name] = airport( aps, name )
        #print(name)
        rx = randint(-w/2,w/2)
        ry = randint(-h/2,h/2)
        data_pts[name] = (rx,ry)
        t.goto(rx,ry)
        t.stamp()

    fls = flights()
    my_fls={}


    # randomize n flights
    cnt=0
    while (cnt < n):
        ap1 = chr(randint(s_char,s_char+n-1))
        ap2 = chr(randint(s_char,s_char+n-1))

        if ap1 is ap2:
            continue

        try:
            p1 = data_pts[ap1]
            p2 = data_pts[ap2]
        except Exception as e:
            print( e )
            continue

        if ap1+ap2 in my_fls:
            continue

        t.goto(p1)
        t.pd()
        t.goto(p2)
        t.pu()

        d = dist(p1,p2)

        my_fls[ap1+ap2] = flight(fls, my_aps[ap1], my_aps[ap2], d)
        my_fls[ap2+ap1] = flight(fls, my_aps[ap2], my_aps[ap1], d)

        cnt+=1

    '''
    # make fully connected
    for i in range(n):
        t.color( random(), random(), random() )
        for j in range( i+1, n ):
            ap1=chr(97+i)
            ap2=chr(97+j)

            p1 = data_pts[ap1]
            p2 = data_pts[ap2]

            t.goto(p1)
            t.pd()
            t.goto(p2)
            t.pd()

            d = dist(p1,p2)

            my_fls[ap1+ap2] = flight(fls, my_aps[ap1], my_aps[ap2], d)
            my_fls[ap2+ap1] = flight(fls, my_aps[ap2], my_aps[ap1], d)
    '''

    '''
    # try it out
    rts = fls.route( my_aps['a'], my_aps['a'] )
    rt = traveling_salesman( aps, rts )
    print_routes( [rt] )
    draw_route( t, rt, data_pts )
    '''

    # try it out
    src = chr(randint(s_char,s_char+n-1))
    dest = chr(randint(s_char,s_char+n-1))

    t.pu()
    t.goto(data_pts[src])
    t.color('blue')
    t.stamp()
    t.goto(data_pts[dest])
    t.stamp()

    fls.print()

    rts = fls.route( my_aps[src], my_aps[dest] )
    print_routes(rts)

    if rts:
        l_rt, l_dist = least_route( rts )
        g_rt, g_dist = greatest_route( rts )

    t.speed(1)
    offset = 0
    for rt in rts:
        #rgb = random(), random(), random()
        d=0
        # should create a route class!
        for fl in rt:
            d+= fl.d

        if l_dist == g_dist:
            rel_dist = 1
        else:
            rel_dist = (d-l_dist)/(g_dist-l_dist)

        rgb = rel_dist, 1-rel_dist, 0

        draw_route( t, rt, data_pts, rgb, offset )
        offset += 5

    t.ht()

    print( 'done' )
    s.mainloop()

if __name__ == '__main__':
    main()