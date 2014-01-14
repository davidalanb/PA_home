

x = 5

class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

def foo():
    global x
    x += 5

def bar( z ):
    z.x = 3

foo()
print(x)

p=point(1,2)
bar(p)
print(p.x)