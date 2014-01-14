


# print the first n multiples of factor f
def print_multiples( f, n ):

    for i in range(1, n+1):
        print(i*f, end='\t' )


#print_multiples( 5, 5 )

'''
# prints multiplication table from 1 to n
def mult_table( n ):

    for i in range(1, n + 1):
        print_multiples( i, n )
        print()
'''

# using nested loops
def mult_table( n ):
    for i in range( 1, n+1 ):
        for j in range( 1, n+1):
            print( i*j, end='\t' )
        print()

mult_table( 5 )



# person defined by name and list of activities
p1 = ( "Mr.B", [ "programming", "climbing", "jamming" ])
p2 = ( "Matt", [ "hiking", "camping", "swimming"])
p3 = ( "Joe", [ "running", "rapping", "dancing" ])

people = [p1, p2, p3]

for person in people:

    print( 'name: ', person[0], end='\nactivities: ' )
    for activity in person[1]:
        print( activity, end=', ' )
    print()


