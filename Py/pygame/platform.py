import pygame
import time
import math

class hero:

    def __init__(self, fn, px, py):
        self.img=pygame.image.load(fn)
        self.orig_sz = self.img.get_size()
        self.px = px
        self.py = py
        self.vx = 0
        self.vy = 0

        self.scale=0.5
        self.resize()

    def update( self, target_surface ):

        w,h = target_surface.get_size()

        if self.px > w/2 or self.px < -w/2:
            self.vx = -self.vx
        if self.py > w/2 or self.py < -w/2:
            self.vy = -self.vy

    def draw( self, target_surface ):
        target_surface.blit(self.img, (self.px - self.w//2 , \
                                        self.py - self.h//2))

    def resize( self):

        self.w = int(self.orig_sz[0]*self.scale)
        self.h = int(self.orig_sz[1]*self.scale)
        self.img=pygame.transform.scale(self.img,(self.w, self.h))


def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((1024,768))

    w,h = main_surface.get_size()

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    #ball = pygame.image.load("ball.png")
    sloth = hero("sloth.png", w//2, h//2)
    sloth.update(main_surface)

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

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
                    pass
                if key == 114:  # rewind
                    pass
                if key == 115:              # 's'
                    pygame.image.save( main_surface, "pygame.jpg")

                if key == 269:
                    sloth.scale-=0.5
                    sloth.resize()
                if key==270:
                    sloth.scale+=0.5
                    sloth.resize()

        # use this for held down key stuff
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            sloth.py -= 5
        if keys[pygame.K_DOWN]:
            sloth.py += 5
        if keys[pygame.K_LEFT]:
            sloth.px -= 5
        if keys[pygame.K_RIGHT]:
            sloth.px += 5

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 100 == 0:
            t1 = time.clock()
            frame_rate = 100 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Copy our image to the surface, at this (x,y) posn
        sloth.draw(main_surface)
        sloth.update(main_surface)

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit()

main()