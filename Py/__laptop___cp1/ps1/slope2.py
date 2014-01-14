def get_user_input():
    x1 = float(input())
    y1 = float(input())
    p1 = x1, y1

    x2 = float(input())
    y2 = float(input())
    p2 = (x2,y2)

    #return a tuple of tuples!
    return (p1,p2)

#(a, b) = get_user_input()
#print( slope(a,b) )

def slope(p1, p2):
    deltaX = p2[0] - p1[0]
    deltaY = p2[1] - p1[1]

    return deltaY / deltaX

(c, d) = ((1,2),(3,4))
print(slope(c,d))

(e,f) = ((5,4),(3,2))
print(slope(e,f))