import math

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.radians()

A = 'A'
B = 'B'
C = 'C'
D = 'D'

cities = [A,B,C,D]

routes = [(A,B,250),(B,C,200),(C,A,150),(A,D,200),(B,D,200)]
a = 200
b = 150
c = 250

#draw AB first
t.stamp()
t.forward( routes[0][2] )
t.stamp()

#calculate position of C based on distances
A = math.acos( (b**2 + c**2 - a**2) / (2*b*c) )
t.goto(0,0)
t.right(A)
t.forward( 150 )
t.stamp()

t.goto(250,0)



s.mainloop()