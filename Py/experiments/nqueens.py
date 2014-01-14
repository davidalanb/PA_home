import math

def nqueens(n):
    # returns true if they're in striking pos
    def danger( pos1, pos2 ):
        if( pos1[0]==pos2[0] or pos1[1:]==pos2[1:] ):
            return True
        elif ( abs(ord(pos1[0]) - ord(pos2[0])) == abs(int(pos1[1:]) - int(pos2[1:])) ):
            return True

        return False

    spots = ['a1']

    # need to place n - 1 more queens
    #for q in range( 0, n-1 ):

    # loop through all positions
    row=98
    while( row<(97+n)):
        col=1
        while(col<(1+n)):

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
                break
            elif(col==n):
                # need to move last placed queen
                lpos=spots.pop()
                row=ord(lpos[0])
                col=int(lpos[1:])

                if( col==n ):
                    lpos=spots.pop()
                    row=ord(lpos[0])
                    col=int(lpos[1:])

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
nqueens(15)
t2=time.time()
print(t2-t1)


