import pygame
import time
import math
import cards
import imp
imp.reload(cards)
from cards import *

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)

    def get_sprite(self, rect):
        return self.sheet.subsurface(rect)

    def get_sprites(self, size):
        width, height = size
        sprites = []

        j = 0
        while j + height <= self.sheet.get_height():
            i = 0
            while i + width <= self.sheet.get_width():

                print( i, j )

                if( i + width > self.sheet.get_width() ):
                    print( 'too wide' )
                    break
                elif( j + height > self.sheet.get_height() ):
                    print( 'too tall' )
                    break
                else:
                    sprites.append( self.sheet.subsurface( (i, j, width, height)))

                i+=width
            j+=height

        return sprites


class PyCards(Game):

    def __init__(self):
        self.deck = Deck()

        ss = Spritesheet( 'cards.png' )
        self.sprites = ss.get_sprites((73,98))

        self.link_sprites()

        #self.deck.shuffle()
        self.hands = self.deck.deal(2, 26)



    def link_sprites(self):

        for i in range(52):
            self.deck.cards[i].sprite = self.sprites[i]


    def play_trick(self):

       # each player plays a card
        p1,p2 = self.hands[0].play()[0], self.hands[1].play()[0]

        print( 'p1:',p1,'\tp2:',p2 )

        if p1.rank == p2.rank:
            print( "War!!!" )

            #TODO:  what happens if a player has no cards left?

            if len(self.hands[0].cards) < 4:
                k1 = self.hands[0].play( len(self.hands[0].cards)-1 )
            else:
                k1 = self.hands[0].play(3)

            if len(self.hands[1].cards) < 4:
                k2 = self.hands[1].play( len(self.hands[1].cards)-1 )
            else:
                k2 = self.hands[1].play(3)

            # now compare cards again - need recursion
            winner = self.play_trick()

            print( '\t', ', '.join(str(card) for card in k1) )
            print( '\t', ', '.join(str(card) for card in k2) )

            self.hands[winner].draw(k1+k2)
            self.hands[winner].draw( (p1,p2) )

            return winner
        elif p1.rank > p2.rank or p1.rank==1:
            print('... p1 wins')
            self.hands[0].draw( (p1,p2) )
            return 0
        else:
            print('... p2 wins')
            self.hands[1].draw( (p1,p2) )
            return 1

    def automate(self):

        self.hands = self.deal( 2, 26 )

        trx = 1
        while( input() == '' ):

            print( '---trick',trx );trx +=1

            self.play_trick()

            print( 'p1:',len(self.hands[0].cards), '\tp2:',
                len(self.hands[1].cards) )

            if len(self.hands[0].cards)==0:
                print( 'Game over - p2 wins!' )
                break
            elif len(self.hands[1].cards)==0:
                print( 'Game over - p1 wins!' )
                break

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((1024,768))

    w,h = main_surface.get_size()

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)


    game = PyCards()
    #game.deck.shuffle()

    ss = Spritesheet( 'cards.png' )
    sprites = ss.get_sprites((73,98))

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()



    while True:

        #start_t = time.clock()

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        #Use the code here for single-press stuff
        if ev.type == pygame.KEYDOWN:
                key = ev.dict["key"]
                print(key)
                if key == 27:                  # On Escape key ...
                    break                      #   leave the game loop
                if key == 112:  # pause / play
                    ball.paused = not ball.paused
                if key == 114:  # rewind
                    ball.d_scale *= -1
                if key == 115:              # 's'
                    pygame.image.save( main_surface, "pygame.jpg")

        # use this for held down key stuff
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            ball.py -= 5
        if keys[pygame.K_DOWN]:
            ball.py += 5
        if keys[pygame.K_LEFT]:
            ball.px -= 5
        if keys[pygame.K_RIGHT]:
            ball.px += 5
        if keys[pygame.K_KP_MINUS]:
            ball.h -= 5
            ball.w -= 5
        if keys[pygame.K_KP_PLUS]:
            ball.h += 5
            ball.w += 5

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 100 == 0:
            t1 = time.clock()
            frame_rate = 100 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # get and draw one card from spritesheet
        #sprite = ss.get_sprite((0,0,73,98))
        #main_surface.blit(sprite, (100,100))

        # draw all sprites cascading
        '''
        pi, pj = 0,0
        for ix, sprite in enumerate(sprites):

            offset = ix//13
            if ix%13==0:
                pi = offset*200
                pj = 0

            main_surface.blit( sprite, (pi, pj) )
            pi += 20
            pj += 20
        '''

        # play cards and draw them
        p1,p2 = game.hands[0].play()[0], game.hands[1].play()[0]

        p1_sprite, p2_sprite = p1.sprite, p2.sprite

        main_surface.blit( p1_sprite, (100,100))
        main_surface.blit( p2_sprite, (300,100))

        # game logic
        if p1.rank == p2.rank:
            the_text = "War!!!"
            winner = random.randint(0,1)
            game.hands[winner].draw((p1,p2))

        elif p1.rank > p2.rank or p1.rank==1:
            the_text = 'P1 Wins'
            game.hands[0].draw( (p1,p2) )
            #return 0
        else:
            the_text = 'P2 Wins'
            game.hands[1].draw( (p1,p2) )
            #return 1




        # Make a new surface with an image of the text
        #the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
        #          .format(frame_count, frame_rate), True, (0,0,0))

        the_text = my_font.render(the_text, True, (0,0,0))

        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

        #end_t = time.clock()
        #dt = start_t - end_t

        # slow down frame rate
        pygame.time.wait(1000)

    pygame.quit()


main()