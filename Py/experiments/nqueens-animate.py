import math
import turtle
s = turtle.Screen()

def draw_chess( t, rows, cols, s ):

    t.seth(0)
    t.pd()

    for i in range(rows):
        for j in range(cols):
            t.right(90)
            t.forward(s)
            t.back(s)
            t.left(90)
            t.forward(s)
        t.right(90)
        t.forward(s)
        t.left(90)
        t.back( s*cols )

def nqueens(n, speed=0):

    # returns true if they're in striking pos
    def danger( pos1, pos2 ):
        if( pos1[0]==pos2[0] or pos1[1:]==pos2[1:] ):
            return True
        elif ( abs(ord(pos1[0]) - ord(pos2[0])) == abs(int(pos1[1:]) - int(pos2[1:])) ):
            return True

        return False

    # setup & draw chess board
    w,h=50,50

    t = turtle.Turtle()
    t.shape('turtle')
    t.pu()
    ul =(-h*n/2, h*n/2)
    t.goto(ul)
    t.speed(0)
    draw_chess(t, n, n, 50)
    t.pu()
    t.speed(speed)

    # initialize spots & stamp
    spots = ['a1']
    ty=ul[1] + -w/2
    tx=ul[0] + h/2
    t.goto( tx, ty )
    sid=t.stamp()
    sids = [ sid ]

    # loop through all positions
    row=98
    while( row<(97+n)):
        col=1
        while(col<(1+n)):

            ty=-(row-97)*w + ul[1] + -w/2
            tx=(col-1)*h + ul[0] + h/2
            t.goto( tx, ty )
            sid = t.stamp()

            p2=chr(row)+str(col)
            #print(p2, end=' ')

            safe=True
            # test against placed queens
            for p1 in spots:
                if( danger(p1,p2)):
                    safe=False
                    break

            if(safe):
                spots.append(p2)
                sids.append( sid )
                break
            elif(col==n):
                # need to move last placed queen
                lpos=spots.pop()
                row=ord(lpos[0])
                col=int(lpos[1:])

                sid2 = sids.pop()
                t.clearstamp(sid2)

                if( col==n ):
                    lpos=spots.pop()
                    row=ord(lpos[0])
                    col=int(lpos[1:])

                    sid2 = sids.pop()
                    t.clearstamp(sid2)

            t.clearstamp(sid)

            col+=1
        row+=1

    #print list
    print(spots)

    # draw board in ASCII
    for row in range(97,97+n):
        for col in range( 1, 1+n):
            pos=chr(row)+str(col)
            if( pos in spots ):
                print( ' Q ', end='' )
            else:
                print( ' - ', end='' )
        print()

import time

t1=time.time()
nqueens(4,3)
t2=time.time()
print(t2-t1)

s.mainloop()
'''
t1=time.time()
nqueens(20)
t2=time.time()
print(t2-t1)
'''