#! /cygdrive/c/Python33/python

'''
Python Chapter 2
'''

# 1. String concat

x = "Hello "
y = "to "
z = "you "

print( x + y + z )

# 2. math

print( 6 * 1 - 2 )
print( 6*(1 - 2) )

# 3. Commented code doesn't execute

# 4. fixing NameError

bruce = 6
print( bruce + 4 )

# 5. Principal

P = 10000
n = 12
r = .08
t = input("number of years?")
t = float(t)

A = P*(1 + r/n)**(n*t)
A = round(A,2)

print( "Balance is now $" + str(A))

# 6. expression 7 % 0 gives ZeroDivisionError

# 7. Alarm goes off at 5pm.  51 % 24 == 3

# 8. Alarm problem

t = int(input("time?"))
h = int(input("house?"))
t += (h%24)

print( "Alarm goes off at " + str(t) )
#  note that this uses 24hr time
