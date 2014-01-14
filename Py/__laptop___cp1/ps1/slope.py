#  Mr. B, August 2013
#  finding slope

'''
# workaround to read from file
import sys
f = open(sys.argv[1],"r")
def input(*args):
    return f.readline()
'''

#begin program
x1 = input()
y1 = input()

x2 = input()
y2 = input()

deltaX = float(x2) - float(x1)
deltaY = float(y2) - float(y1)

slope = deltaY / deltaX
print( slope )