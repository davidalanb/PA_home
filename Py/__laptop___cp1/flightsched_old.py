

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

        # first pass
        for fl in self.fls:
            if fl.src == src:
                if fl.dest == dest:
                    paths.append([fl])
                else:
                    maybe.append([fl])
                    fl2 = self.route_h( fl.dest, dest )
                    if fl2:
                        maybe[-1].append(fl2)
                        paths.append(maybe[-1])

        return paths

    def route_h(self, src, dest):

        for fl in self.fls:
            if fl.src == src:
                if fl.dest == dest:
                    return fl
                else:
                    None


def main():
    bos = airport( "Boston" )
    chi = airport( "Chicago" )
    nyc = airport( "New York" )
    lax = airport( "Los Angeles" )

    fls = flights()

    f1 = flight( fls, bos, chi, 982 )
    f2 = flight( fls, chi, bos, 982 )

    f3 = flight( fls, bos, lax, 3036 )
    f4 = flight( fls, chi, lax, 2112 )

    fls.print()

    print('---' )
    rts = fls.route( bos, lax )
    for i, rt in enumerate(rts):
        print( "--- route",i )
        for fl in rt:
            fl.print()

main()