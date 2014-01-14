class Account:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.balance = 0


    def withdraw( self,amt ):
        self.balance -= amt

    def deposit( self,amt ):
        self.balance += amt

    def balance( self ):
        return self.balance



a = Account()

a.deposit( 100 )

print( a.balance )