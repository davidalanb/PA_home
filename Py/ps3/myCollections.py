# printing collections

def print_lines( c ):
    for item in c:
        print( item )

def print_line( c, d ):
    for item in c:
        print( item, end=d )
    print()


def print_table( list ):
#    for n, val in enumerate(list):
#        print( n, '\t', val )
    for i in range(len(list)):
        print( i, '\t', list[i] )

#-----------------------------------

def arithmetic( a, b, n ):
    my_list = []
    for i in range( n ):
        my_list.append( a + b*i )
    return my_list

def geometric( a, b, n ):
    my_list = []
    for i in range(n):
        my_list.append( a*b**i )
    return my_list

def my_sum( list ):
    return sum( list )


#--------------------------------------


def sequence( li, ui, foo ):
    ret = []
    for i in range( li, ui ):
        ret.append( foo( i ) )
    return ret

'''
def summation(start_n, end_n, foo ):
    sum=0
    for i in range( start_n, end_n ):
        sum += foo(i)
    return sum
'''

#-----------------------------------

# print a chess board using ASCII
def chess( rows, cols):
    print( '----'*cols+'-')
    for i in range(rows):
        for j in range(cols):
            print( '|   ', end='' )
        print('|')
        print( '----'*cols+'-')

# prints an n X n multiplication table
# starting at 1 and ending at n
def mult_table(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print( i*j, end='\t' )
        print()


#--------------------- testing --------------

if __name__=='__main__':
    chess(2,3)

    mult_table( 3 )
