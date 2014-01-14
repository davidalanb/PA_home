
import threading

def f(n=0):
    # do something here ...
    print(n)
    # call f() again in 60 seconds
    return threading.Timer(1, f,[n+1]).start()



# start calling f now and every 60 sec thereafter
t = f()



while( 1 ):
    print( "infinite loop" )