import sys
import imp
import turtle
from PIL import ImageGrab

def testMath(p,f):

    myMath=imp.load_source('myMath',p+'/myMath.py')

    print('\t\t'+str(myMath.distance((3,0), (8,5))), file=f)
    print('\t\t'+str(myMath.circle_area(1)), file=f)
    print('\t\t'+str(myMath.quadratic(1, 3, 2)), file=f)


#f=open("asdf.txt",'w')
#testMath('ComputerProgramming1_15964501/temp/Comeau_Samantha_115004_Program Set 2',f )
#testMath('ComputerProgramming1_15964501/temp/Burgess_Gavin_118703_Programme Set 2',f )


def testTurtle(p,f):
    #installed Pillow for screen capture
    #https://pypi.python.org/pypi/Pillow/2.1.0#downloads

    myTurtle=imp.load_source('myMath',p+'/myTurtle.py')

    wn = turtle.Screen()
    t = turtle.Turtle()

    t.speed(0)
    myTurtle.draw_axes( wn, t )
    t.speed(0)
    myTurtle.draw_name( wn, t )
    t.speed(0)
    myTurtle.draw_line( wn, t, -3, 5 )

    t.speed(0)
    t.pu()
    t.goto( 100, 100 )
    t.pd()
    myTurtle.draw_triangle( wn, t, 50 )

    t.speed(0)
    t.pu()
    t.goto( 100, -100 )
    t.pd()
    myTurtle.draw_square( wn, t, 50 )

    t.speed(0)
    t.pu()
    t.goto( -100, 100 )
    t.pd()
    myTurtle.draw_pent( wn, t, 50 )

    name=p.split('/')[-1]
    ImageGrab.grab().save(name+'.jpg', "JPEG")

    turtle.bye()
    print('\t\tmyTurtle finished.',file=f)
    #sys.path.remove( p )
