
import math

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c
x1 = (-1*b + math.sqrt(d))/(2*a)
x2 = (-1*b - math.sqrt(d))/(2*a)

print( x1 )
print( x2 )