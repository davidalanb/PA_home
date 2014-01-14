
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

    return rts[ix]

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

def main():

    aps = airports()
    bos = airport( aps, "Boston" )
    chi = airport( aps, "Chicago" )
    nyc = airport( aps, "New York" )
    lax = airport( aps, "Los Angeles" )
    dal = airport( aps, "Dallas" )

    fls = flights()

    f1 = flight( fls, bos, lax, 3036 )
    f4 = flight( fls, bos, nyc, 213 )
    f2 = flight( fls, bos, chi, 982 )

    f7 = flight( fls, nyc, chi, 840 )
    f5 = flight( fls, nyc, dal, 1604 )
    f12 = flight( fls, nyc, bos, 213 )

    f10 = flight( fls, chi, nyc, 840 )
    f3 = flight( fls, chi, lax, 2112 )
    f0 = flight( fls, chi, dal, 931 )

    f8 = flight( fls, dal, nyc, 1604 )
    f9 = flight( fls, dal, chi, 931 )
    f6 = flight( fls, dal, lax, 1425 )

    f11 = flight( fls, lax, dal, 1425 )


    print('Routes - BOS to LAX' )
    rts = fls.route( bos, lax )
    print_routes( rts )
    print()

    print('Least route - BOS to LAX')
    rt = least_route( rts )
    print_routes( [rt] )
    print()

    print('Round-trips - DAL')
    rts = fls.route(dal,dal)
    print_routes( rts )
    print()

    print("Traveling Salesman - DAL")
    rt = traveling_salesman( aps, rts )
    print_routes( [rt] )

main()