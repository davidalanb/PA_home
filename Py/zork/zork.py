
class Confusion( Exception ):
    def __init__(self):
        super().__init__()

class CLI():
    help = { "go": "use 'go [ N | E | S | W ]'",\
            "look": "use 'look' to see what items are available\n"+ \
                    "use 'look <item>' to inspect an item more closely",
            "quit": "use 'quit' to exit.  progress won't be saved!"}
    def __init__(self):
        pass

    def interpret(self, player):

        p = player

        while(1):

            print( '>', end=' ' )
            cmd = input()
            print()
            tokens = cmd.lower().split(' ')

            for token in tokens:
                if token in ['the', 'at', 'a']:
                    print(token)
                    tokens.remove(token)

            print('--'+' '.join(tokens))

            try:

                if tokens[0] == 'help':
                    if len(tokens) > 1:
                        if tokens[1] in CLI.help.keys():
                            print( CLI.help[tokens[1]] )
                        else:
                            raise Confusion
                    else:
                        print( "help on which command?\n",\
                    "use 'help [go | look | quit]'")

                elif tokens[0] == 'go':
                    if len(tokens) > 1:
                        if tokens[1][0] in ['n','e','s','w']:
                            p.go(tokens[1].upper()[0])
                            break
                        else:
                            raise Confusion
                    else:
                        print("go where?")

                elif tokens[0] == 'look':
                    if len(tokens)>1:
                        p.look_at( ' '.join(tokens[1:len(tokens)]))
                    else:
                        p.loc.show_items()

                elif tokens[0] == 'take':
                    if len(tokens)>1:
                        p.take( ' '.join(tokens[1:len(tokens)]))
                    else:
                        print("take what?")

                elif tokens[0] == 'check':
                    if len(tokens)>1:
                        p.check(' '.join(tokens[1:len(tokens)]))
                    else:
                        print("check what?")

                elif tokens[0] == 'quit':
                    #save()
                    print(" you'll be back... ")
                    break

                else:
                    raise Confusion

            except Confusion:
                print( "I don't understand.")

class Player():
    def __init__(self):
        self.loc = None
        self.cli = CLI()
        self.map = Map()
        self.backpack = {}

    def enter(self, rm):
        self.loc = rm

        rm.enter()
        if not rm.visited:
            rm.add_to_map()

        self.cli.interpret(self)

    def go(self, dir):
        if dir in self.loc.links.keys():
            self.enter( self.loc.links[dir] )
        else:
            print( "ouch!  you ran into a wall." )
            self.cli.interpret(self)

    def look_at( self, item_name ):

        itms = self.loc.items
        hdn = self.loc.hidden

        if item_name in itms.keys():
            if type(itms[item_name]) is str:
                print(itms[item_name])
            else:
                if itms[item_name]:
                    print( "You see", ', '.join(itms[item_name]) )
                else:
                    print( "you took everything" )
        elif item_name in hdn.keys():
            print( itms[hdn[item_name]][item_name] )
        else:
            print("none of those here")
        pass

    def take( self, item_name ):

        if item_name in self.loc.hidden.keys():

            found = self.loc.hidden.pop(item_name)
            self.loc.items[found].pop(item_name)

            print( "taking",item_name )
            self.backpack[item_name] = found
        elif item_name in self.loc.items.keys():
            print("too heavy")
        else:
            print("none of those here")
        pass

    def check( self, item_name):

        if item_name == "backpack":
            if self.backpack:
                print( "you have",', '.join(self.backpack))
            else:
                print( "you have nothing." )

class Map():
    def __init__(self):
        self.map = ''


class Room():
    def __init__(self, id, name, desc='' ):
        self.id = id
        self.name = name
        self.cli = CLI()
        self.links = {}
        self.visited = False
        self.items= {}
        self.hidden={}
        self.desc = desc
        pass

    def add_link( self, rm, dir, r=True ):

        self.links[dir] = rm

        if r:
            # make all links 2-way
            if dir=='N':
                opp = 'S'
            elif dir=='S':
                opp='N'
            elif dir=='E':
                opp='W'
            elif dir=='W':
                opp='E'

            rm.add_link( self, opp, False )

    def enter(self):

        print( "You enter ", self.name )

        if not self.visited:
            print( self.desc )
            '''
            for key in self.links:
                print( "To the", key, "is",\
                self.links[key].name)
            '''
            self.visited = True


    def add_to_map():
        pass

    def add_items(self, itms):
        self.items = dict(list(self.items.items()) + list(itms.items()))

        for key,itm in itms.items():
            if type(itm) is dict:
                for key2,itm2 in itm.items():
                    self.hidden[key2]=key

    def add_hidden(self, ls):
        self.hidden = dict(list(self.hidden.items()) + list(ls.items()))

    def show_items(self):
        if self.items:
            ks=self.items.keys()
            print( "You notice", ', '.join(ks))
        else:
            print("the room is pretty bare")


class Zork():

    rooms = {}

    def __init__(self):
        pass

        #cli = CLI()

        self.ballrm = Room(1, "ballroom", "It doesn't look like there's"+\
        " been a party here in a while." )
        self.dining = Room(2, "dining room","Smells like rotten food" )
        self.kitch = Room(3, "kitchen","The staff here must have served a lot"+\
         " of guests at one time" )
        self.game = Room(4, "game room","There must have once been a nice "+\
        "casual atmosphere here." )
        self.dying = Room(5, "dying room","Smells like death.")


        self.dying.add_link( self.kitch, 'S' )
        self.ballrm.add_link( self.game, 'N' )
        self.game.add_link( self.kitch, 'E' )
        self.kitch.add_link( self.dining, 'S' )
        self.ballrm.add_link( self.dining, 'E' )


        self.game.add_items({"pool table":{"8 ball":"round","broken cue":"sharp"},\
                            "poker table":"not sure if the deck is full",\
                            "bar":"good thing you quit drinking"})

        self.dying.add_items({"altar":{"skull":"the bone is charred","knife":"jewel encrusted"}})

        #self.game.add_hidden({"8 ball":"pool table","broken cue":"pool table"})
        #self.dying.add_hidden({"skull":"the altar","knife":"the altar"})


        self.p1 = Player()

    def run(self):

        print( "You enter the forlorn mansion through the south ballroom door.")
        print( "The door seals behind you." )

        self.p1.enter(self.ballrm)
        #self.ballrm.enter()

def main():
    z = Zork()
    z.run()

if __name__=='__main__':
    main()
