

x = 5

if( x < 0 ):
    print( "x is negative" )
elif( x == 0):
    print( "x is zero" )
else:
    print( "x is positive" )


if x >= 0:
    if x == 0:
        print("x is zero")
    else:
        print("x is positive")

else:
    print("x is negative")


def safe_division( a, b ):
    if( type(a) is str and a.isnumeric() ):
        a = float(a)

    if( type(b) is str and b.isnumeric() ):
        b = float(b)

    if (( type(a) is float ) or (type(a) is int)) and \
    (( type(b) is float ) or (type(b) is int)) :

        if b == 0:
            return "undefined"
        else:
            return a / b

    else:
        return "invalid input"

q = safe_division( 5, 0 )
print(q)

q = safe_division( "5", 3 )
print(q)


