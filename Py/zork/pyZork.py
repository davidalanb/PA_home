class CLI:

    def __init__(self):
        self.cmds = {}

    def add_cmd(self, cmd, action):
        self.cmds[cmd] = action

    def run_cmd(self, cmd, params=[]):

        self.cmds[cmd](params)
        '''
        try:
            self.cmds[cmd](params)

        except Exception as e:
            print( type(e), ':', e )
        '''
    def start(self):

        self.running = True

        while(self.running):
            print('>')
            cmd = input().lower()
            # tokenize
            tokens = cmd.split(' ')
            if tokens[0] in ['exit','quit','bye']:
                print( 'bye' )
                break
            # process
            if len(tokens)>1:
                self.run_cmd( tokens[0], tokens[1:] )
            else:
                self.run_cmd( tokens[0], [] )


    def stop(self):
        self.running = False

    def help(self, params):
        print( 'commands:' )
        for cmd in self.cmds:
            print( '\t>',cmd )

class Room:

    def __init__(self, n='', d="", connects={}):
        self.name = n
        self.description = d
        self.items = {}
        self.containers = {}
        self.connections = {}
        self.locked = False
        self.key = None

        self.enemy = None

        for rm,d in connects:
            self.connect( rm, d )

    def connect( self, rm2, direct ):
            self.connections[ direct ] = rm2

            opp = {'n':'s','e':'w','s':'n','w':'e'}

            if opp[direct] not in rm2.connections:
                rm2.connections[ opp[direct] ] = self

    def add_items( self, stuff ):
        self.items.update( stuff )

    def add_containers( self, stuff ):
        self.containers.update( stuff )

    def add_enemy( self, enemy ):
        self.enemy = enemy

    def enter( self ):

        print( "You have entered",self.name )
        print(self.description)
        if self.enemy:
            print( self.enemy.description )

        #self.print_detail()

    def print_detail( self ):
        #print( "You have entered",self.name )
        if self.connections:
            for direction, room in self.connections.items():
                print( 'To the',direction.upper(),'lies',room.name )

    # show enemies here too
    def inspect( self ):
        # connections
        self.print_detail()

        has_stuff = False
        if self.enemy:
            has_stuff = True
            print( self.enemy.description )

        # items
        if self.items:
            has_stuff = True
            print( 'you see', end=' ')
            for i, key in enumerate(self.items):
                if i == len(self.items)-1:
                    print( 'and', end=' ')
                print( 'a', key, end=' ' )
            print()
            '''
            sorted_items = sorted(self.items.keys())
            if len(sorted_items) > 1:
                sorted_items.insert(-1,'and')
            print( 'you see a', ', '.join(sorted_items))
            '''
        # containers
        if self.containers:
            has_stuff = True
            sorted_items = sorted(self.containers.keys())
            if len(sorted_items) > 1:
                sorted_items.insert(-1,'and')
            print( 'you see a', ', '.join(sorted_items))

        if not has_stuff:
            print( "There's not much in here.\nSomeone may have cleaned it out" )


class Container:
    def __init__(self, name, description, items={} ):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        ret = self.description
        #for name in self.items:
        #    ret += name
        return ret

    def add_items(self, stuff):
        self.items.update(stuff)

class Enemy:

    def __init__(self, name, description, weakness=None ):
        self.name = name
        self.description = description
        self.weakness = weakness

    def set_weakness(self, weakness):
        self.weakness = weakness


class Player:

    def __init__(self, location=None, items={}):
        self.location = location
        self.items = items

    def set_cli( self, cli ):
        self.cli = cli

    def goto( self, rm ):
        self.location = rm
        self.location.enter()

    def go(self, params):

        dest = self.location.connections[params[0][0]]

        if dest.locked:
            print( 'The door is locked' )
            if dest.key in self.items.keys():
                print( "You've used", dest.key )
                dest.locked = False
                self.go( [params[0]])
        else:
            self.location = dest
            self.location.enter()
        #print( self.location.get_str() )
        #self.look()

    def look( self, params=[]):
        #print( self.location.get_str() )
        if params:
            if params[0] in self.location.items:
                print( self.location.items[params[0]] )
            elif params[0] in self.location.containers:
                print( self.location.containers[params[0]])
            else:
                self.location.inspect()
        else:
            self.location.inspect()

    def take( self, params ):
        if params:
            name = params[0]
            if name in self.location.items:
                desc = self.location.items[name]
                self.items[name]=desc
                del self.location.items[name]

                print( 'you have taken the', name )
            else:
                for container in self.location.containers.values():
                    if name in container.items:

                        desc = container.items[name]
                        self.items[name]=desc
                        del container.items[name]

                        print( 'you have taken the', name )

        else:
            print( 'take what?' )

    def inv( self, params ):
        if self.items:
            print( 'you have',', '.join(self.items))
        else:
            print( 'you have nothing' )

    def use( self, params ):
        # use on enemy
        if params[0] in self.items and params[0] == self.location.enemy.weakness:
            print( 'You have slayed the', self.location.enemy.name )
            self.location.enemy = None

        elif params[0] in self.items and params[0] != self.location.enemy.weakness:
            self.die( 'you have fallen to the ' + self.location.enemy.name +  '.\n'+
                'next time choose your weapon more carefully.')

    def die( self, message ):
        print( message )
        self.cli.stop()



class Game:

    def __init__(self):

        self.rms = {}
        self.p1 = Player()
        self.cli = CLI()

    def init(self):

        '''
        NW Room  |  NE Room     -  Dungeon
        ---------|--------------
        SW Room  |  SE Room

        '''

        #------------ initialize rooms and connections
        roomlist = { "Library":"The old library is disheveled.",
                    'Idol Room':'This room is filled with strange things.',
                    'Music Room':'This room was once filled with music.',
                    'Courtyard':'This large hall must have once been grand.',
                    'Dungeon':'This room reeks of death.' }
        self.add_rooms(roomlist)

        self.rms['Dungeon'].locked=True
        self.rms['Dungeon'].key = 'dragon-key'

        connections = { "Library": {'n':'Music Room', 'w':'Courtyard'},
                        "Idol Room": {'e':'Music Room', 's':'Courtyard'},
                        'Music Room': {'e':'Dungeon'} }
        self.add_connections(connections)

        #------------ add items
        itemlist = { "Library": { "book":"the pages are torn",
                            "calendar":"dated 1923" },
                    "Idol Room": { 'dragon-key': 'this key is shaped like a dragon!',
                        'shrunken-shead':"it's all shriveled up"},
                    "Music Room": { 'piano':'it needs to be tuned' }}

        self.add_items( itemlist )

        #---------- add containers / items

        statue = Container('statue',"The statue is a knight in armor holding a large sword")
        statue.add_items({'sword':'made of steel'})
        self.rms['Courtyard'].add_containers( { 'statue': statue } )

        #--------------- add enemy

        # props to: http://www.seventhsanctum.com/generate.php?Genname=dragondesc
        dragon = Enemy('Dragon', "This dragon has an elegant, elongated body. \n"+
        "Its scales are sand-colored. On the end of its tail is a hooklike extension. \n"+
        "This dragon has six short limbs with six closely-mounted digits on each foot \n"+
        "that end in long, sharp claws. It has small wings running from its shoulders \n"+
        "to its hips. This dragon's head is elongated and it has a wide mouth with \n"+
        "fine, sharp teeth. It has deep-set eyes that are the color of valuable \n"+
        "emeralds. A bony plate projects from the back of its skull, protecting its \n"+
        "upper neck Bladelike bony plates sprout from its chin. \n"+
        "Two horns extend from its forhead.", 'sword')
        self.rms['Dungeon'].add_enemy( dragon )

        #------- spawn player
        self.p1.goto(self.rms['Courtyard'])
        self.p1.set_cli(self.cli)

        #------------------------- setup CLI
        self.cli.add_cmd( 'go', self.p1.go )
        self.cli.add_cmd( 'look',self.p1.look )
        self.cli.add_cmd('take',self.p1.take )
        self.cli.add_cmd('inv',self.p1.inv )
        self.cli.add_cmd('help',self.cli.help )
        self.cli.add_cmd('use',self.p1.use )

    def add_rooms(self, roomlist ):
        # add rooms - gen_purpose

        for name, desc in roomlist.items():
            self.rms[name] = Room( name, desc )

    def add_connections(self, connections):
        # add connections - gen_purpose
        for r1,c in connections.items():
            for d,r2 in c.items():
                self.rms[r1].connect(self.rms[r2],d)

    def add_items(self, itemlist):
        for rm, itms in itemlist.items():
            self.rms[rm].add_items( itms )

    def print_rooms(self):
        for rm in self.rms:
            print( rm.get_str() )

    def start( self ):
        self.cli.start()

def main():

    g = Game()
    g.init()
    g.start()

main()
