#--- myMath.py ----
import math

#----------circle_area -----------

def circle_area( r ):
    return math.pi*r**2

#----------distance---------------


def distance( p1, p2 ):
    x1,y1=p1
    x2,y2=p2
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

#-------------- quadratic

def quadratic( a, b, c ):
    sqrt_d = math.sqrt( b**2 - 4*a*c )
    x1 = (-b + sqrt_d)/(2*a)
    x2 = (-b - sqrt_d)/(2*a)
    return (x1, x2 )

#--------------- testing

# combine the previous 4 statements into one!
#print( distance( (1,2),(3,4)))