class CLI:

    def __init__(self):
        self.cmds = {}

    def add_cmd(self, cmd, action):
        self.cmds[cmd] = action

    def run_cmd(self, cmd, params=[]):
        try:
            self.cmds[cmd](params)

        except Exception as e:
            print( type(e), ':', e )

    def start(self):

        while(1):
            cmd = input()
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


# very basic Person class
class Person():
    def __init__(self,name):
        self.name=name

    # this method will be called via the CLI
    def say_hi(self, params):
        print( "Hi, I'm", self.name )
        print( '\tparams: ', params )

# if we're running this script
if __name__=='__main__':

    # instantiate new CLI and Person
    cli = CLI()
    p = Person('Joe')

    # link CLI command 'hi' to say_hi method
    cli.add_cmd('hi',p.say_hi)

    # run the CLI
    # by default exit on 'exit', 'bye', or 'quit'
    cli.start()