class Person:
    def __init__(self, n="Anonymous" ):     # constructor
        self.name = n
        self.hobbies=[]

    def say_hello( self ):
        print( "Hi, my name is", self.name )

        if self.hobbies:
            print( "I like", ', '.join(self.hobbies) )

    def add_hobby( self, hobby ):
        self.hobbies.append(hobby)

class Town:
    def __init__(self):
        joe = Person("Joe")          # define a Person object
        joe.add_hobby( "playing guitar" )
        joe.add_hobby( "running" )
        r = Person( "Rebekah" )

        self.people = [ joe, r ]

    def hi_guys(self):
        for p in self.people:
            p.say_hello()

def main():
    t = Town()
    t.hi_guys()

main()



