'''
myConditionals.py
'''

'''
prints a truth table,
op: a string specifying the operation (and, or, not)
other input should print "operation not supported"
'''
def print_tt( op ):

    if op == 'and':
        print( "a\t\t b\t\t a and b")
        for a in (False, True):
            for b in (False, True):
                print( a, '\t', b, '\t', (a and b))

    elif op == 'or':
        print( "a\t\t b\t\t a or b")
        for a in (False, True):
            for b in (False, True):
                print( a, '\t', b, '\t', (a or b))

    elif op == 'not':
        print( "a\t\t not a")
        for a in (False, True):
            print( a, '\t', (not a))

    else:
        print( '#operator', op, 'not supported' )


def safe_division( a, b ):
    try:
        a = float(a)
        b = float(b)

    except:
        print( '#invalid input' )
        return

    if b==0:
        print( '#zero division' )
        return

    return a / b

def get_float():
    inp = input('> ')

    while(True):
        try:
            inp=float(inp)
            break
        except:
            print('try again')
            inp=input('> ')

    return inp



def find_sub( s, sub ):

    ixs = []
    ix = s.find(sub)

    while( ix != -1 ):
        ixs.append(ix)
        ix = s.find(sub, ix+1)

    return ixs




#print(get_float())

'''
takes a string
'''
def is_palindrome( s ):

    if type(s) is not str:
        print( "invalid input" )
        return

    s=s.lower().replace( ' ','' )

    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return False

    return True

def factorize( a ):

    factors=[]

    if a < 0:
        a = int(-a)
        factors.append(-1)

    left = a
    while( left > 1 ):

        # try to divide by numbers less than 'left'
        for i in range( 2, left+1 ):

            if left % i == 0:
                factors.append(i)
                left = left // i
                break

    return factors


def is_prime( n ):

    if type(n) is not int or n < 2:
        return

    for i in range(2, n//2+1):
        if n%i == 0:
            return False

    return True

def get_primes( n ):
    primes=[]

    i, cnt=0,0
    while( cnt < n ):
        if is_prime( i ):
            primes.append(i)
            cnt+=1
        i+=1

    return primes

if __name__=="__main__":

    import time

    print( '\n--- safe math ---\n' )
    print( safe_division( 5, 0.0 ) )
    print( safe_division( 5, '0.0' ) )

    print( safe_division( '5', '2.0' ) )
    print( safe_division( 5, 1.23 ) )

    print( '\n--- find sub ---\n' )

    my_str = "I'm trying to think of a sentence \
    which has a lot of occurrences \
    of a particular substring in it..."
    ixs = find_sub(my_str, 'in' )
    print( ixs )

    for ix in ixs:
        print( ix, my_str[ix:(ix + 2)] )

    print( '\n--- palindrome ---\n' )
    print( is_palindrome( "race car" ) )
    print( is_palindrome( "a man a plan a canal panama" ) )
    print( is_palindrome( "this is a test" ))

    print( '\n--- primes ---\n' )
    for i in range(2, 25):
        if( is_prime( i ) ):
            print( i, end=', ' )
    print()

    print( '\n--- factorize ---\n' )

    t1 = time.time()
    print( factorize( 138562 ) )
    t2 = time.time()

    print( get_primes(1000)[999] )

    #print( t2 - t1 )

