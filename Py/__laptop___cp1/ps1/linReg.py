print( "x1: " )
x1 = float(input())
print( "y1: " )
y1 = float(input())
print( "x2: " )
x2 = float(input())
print( "y2: " )
y2 = float(input())

deltaX = x2 - x1
deltaY = y2 - y1

m = deltaY / deltaX
print( "slope: " + str(m))

b = y1 - m*x1
print( "y-intercept: " + str(b))

print( "equation: Y = " + str(m) + "X + " + str(b) )

print( "enter X to approximate Y: " )
x = float(input())
y = m*x + b

print( "approximation for Y: " + str(y))
