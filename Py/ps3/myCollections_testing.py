'''
Program set 3 - testfile
Name:

Comment out testing you're not ready to run yet
Include any additional testing you design
'''

#-------------- imports

import myCollections
import imp
imp.reload(myCollections)
from myCollections import *

#--------------- testing

print( "\n=== BASIC TESTING ===\n")

stuff = ['a','b','c']
print( stuff )
print( stuff[0], stuff[1], stuff[2] )
print_lines( stuff )
print_line( stuff, '.' )
print( '-------------' )

print( "\n=== SEQUENCES & TABLES ===\n")

print( "table with indices:\n")
print( 'n\ta-sub-n' )
print_table( stuff )
print( '-------------' )

print( "arithmetic & sum:\n")
a = arithmetic( 1, 2, 3 )
print( a )
print( 'sum: ', my_sum( a ) )
print( '-------------' )

print( "geometric & table:\n")
g = geometric( 1, 2, 5 )
print( 'n \t a-sub-n' )
print_table( g )
print( '-------------' )

print( "2D tables:\n")
mult_table(10)
print()
chess(8,8)

# -----------advanced testing

'''
def square( n ):
    return n**2
print( sequence(1, 5, square )  )

# a lambda is a function of x that we're defining on the fly
print( sum(sequence( 1, 1000, lambda x: 1/2**x)))
'''
