import sys
import imp
import turtle
from PIL import ImageGrab

def testMath(p,f):

    try:
        myMath=imp.load_source('myMath',p+'/myMath.py')
    except Exception as e:
        print('\t\t',e, file=f)
        
    try:
        print('\t\t'+str(myMath.distance((3,0), (8,5))), file=f)
    except Exception as e:
        print('\t\t',e, file=f)
    
    try:
        print('\t\t'+str(myMath.circle_area(1)), file=f)
    except Exception as e:
        print('\t\t',e, file=f)
    
    try:
        print('\t\t'+str(myMath.quadratic(1, 3, 2)), file=f)
    except Exception as e:
        print('\t\t',e, file=f)

def my_goto(t,x,y):
    t.pu()
    t.goto( x, y )
    t.speed(0)
    t.pd()
    
def testTurtle(p,f):
    #installed Pillow for screen capture
    #https://pypi.python.org/pypi/Pillow/2.1.0#downloads

    try:
        myTurtle=imp.load_source('myMath',p+'/myTurtle.py')
    except Exception as e:
        print('\t\t',e, file=f)
        
    wn = turtle.Screen()
    t = turtle.Turtle()
    
    t.speed(0)
    try:
        myTurtle.draw_name( wn, t )
    except Exception as e:
        print('\t\t',e, file=f)
    
    t.speed(0)
    try:
        myTurtle.draw_axes( wn, t )
    except Exception as e:
        print('\t\t',e, file=f)
    
    t.speed(0)
    try:
        myTurtle.draw_line( wn, t, -3, 5 )
    except Exception as e:
        print('\t\t',e, file=f)
      
    my_goto( t,200, 200 )
    try:
        myTurtle.draw_triangle( wn, t, 50 )
    except Exception as e:
        print('\t\t',e, file=f)
        
    my_goto( t,200, -200 )
    try:
        myTurtle.draw_square( wn, t, 50 )
    except Exception as e:
        print('\t\t',e, file=f)
        
    my_goto( t,-200, 200 )
    try:
        myTurtle.draw_pent( wn, t, 50 )
    except Exception as e:
        print('\t\t',e, file=f)
        
    try:
        name=p.split('/')[-1]
        ImageGrab.grab().save(name+'.jpg', "JPEG")
    except Exception as e:
        print('\t\t',e, file=f)

    turtle.bye()
    print('\t\tmyTurtle finished.',file=f)
