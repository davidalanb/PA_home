class test:

    y = []

    def __init__(self, x):
        self.x = x


t1 = test(1)
t2 = test(2)

t1.y.append( 'asdf' )
test.y.append('fd')
t2.y.append( 'fni' )

print(t1.x, t1.y, t2.x, t2.y)