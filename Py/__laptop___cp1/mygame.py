import pygame
import time

class rect:
    def __init__(self, px, py, w, h ):
        self.h = h
        self.w = w
        self.px = px
        self.py = py

    def update(self):
        return

    def draw(self, target_surface):
        target_surface.fill((255,0,0), (self.px, self.py, self.w, self.h))

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((800,600))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("ball.png")

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    s1 = rect(300,100,150,90)

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop



        ''' Use the code here for single-press stuff

        if ev.type == pygame.KEYDOWN:
                key = ev.dict["key"]
                print(key)
                if key == 27:                  # On Escape key ...
                    break                      #   leave the game loop.
                elif key==269:                  # num -
                    s1.h -= 10
                    s1.w -= 10
                elif key==270:                  # num +
                    s1.h += 10
                    s1.w += 10
                elif key==273:                  # up
                    s1.py -= 10
                elif key==274:                  # down
                    s1.py += 10
                elif key==275:                  # right
                    s1.px += 10
                elif key==276:                  # left
                    s1.px -= 10
        '''

        # use this for held down key stuff
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            s1.py -= 1
        if keys[pygame.K_DOWN]:
            s1.py += 1
        if keys[pygame.K_LEFT]:
            s1.px -= 1
        if keys[pygame.K_RIGHT]:
            s1.px += 1
        if keys[pygame.K_KP_MINUS]:
            s1.h -= 1
            s1.w -= 1
        if keys[pygame.K_KP_PLUS]:
            s1.h += 1
            s1.w += 1

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 100 == 0:
            t1 = time.clock()
            frame_rate = 100 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Put a red rectangle somewhere on the surface
        #main_surface.fill((255,0,0), (300, 100, 150, 90))
        s1.draw(main_surface)

        # Copy our image to the surface, at this (x,y) posn
        main_surface.blit(ball, (100, 120))

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

        # slow down frame rate
        pygame.time.wait(int(1000/60))

    pygame.quit()


main()