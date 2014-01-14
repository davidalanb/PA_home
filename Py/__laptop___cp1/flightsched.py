

class airport:

    def __init__( self, name ):
        self.name=name

class flight:

    def __init__( self, fls, src, dest, d ):
        self.src = src
        self.dest = dest
        self.d = d

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

        '''
        # need to recurse here I think
        for route in maybe:
            fl = route[-1]
            fl2 = self.route_h( fl.dest, dest, rest[:] )
            if fl2:
                route.append(fl2)
                paths.append(route)
                maybe.remove(route)
            else:
                # its still a maybe, so
                # route.append(fl2)
                # recurse on fl2
                #  when do we bail?
                None
        '''
        self.route_r( paths, maybe, rest, dest )

        return paths

    def route_r(self, paths, maybe, rest, dest ):
        loc_maybe=[]
        loc_rest=[]

        for route in maybe:
            fl = route[-1]

            for fl2 in rest:
                if fl2.src == fl.dest:
                    if fl2.dest == dest:
                        route.append(fl2)
                        paths.append(route)
                    else:
                        loc_route = route[:]
                        loc_route.append(fl2)
                        loc_maybe.append(loc_route)
                        self.route_r( paths, loc_maybe, loc_rest, dest )
                else:
                    loc_rest.append(fl2)

def main():
    bos = airport( "Boston" )
    chi = airport( "Chicago" )
    nyc = airport( "New York" )
    lax = airport( "Los Angeles" )
    dal = airport( "Dallas" )

    fls = flights()

    f1 = flight( fls, bos, lax, 3036 )
    f2 = flight( fls, bos, chi, 982 )
    f3 = flight( fls, chi, lax, 2112 )
    f4 = flight( fls, bos, nyc, 213 )
    f5 = flight( fls, nyc, dal, 1604 )
    f6 = flight( fls, dal, lax, 1425 )
    f7 = flight( fls, nyc, chi, 840 )

    fls.print()

    print('---' )
    rts = fls.route( bos, lax )
    for i, rt in enumerate(rts):
        print( "--- route",i )
        for fl in rt:
            fl.print()

main()