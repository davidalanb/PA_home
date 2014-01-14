import pygame
import time

class Paddle:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y,150, 25)
        #self.x = x
        #self.y = y

    def draw( self, target_surface ):
        target_surface.fill((255,0,0), self.rect)

    def move( self, dx, dy ):
        #self.x += dx
        #self.y += dy
        self.rect = self.rect.move( dx, dy )

def main():

    #-------------- INITIALIZE

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((800, 600))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale( ball, (50,50) )

    paddle = Paddle(400,550)

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    #-------------- GAME LOOP
    while True:

        #--------------- EVENT POLLING ----------------------------

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop




        # discover held down keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move( -1, 0 )
        if keys[pygame.K_RIGHT]:
            paddle.move( 1, 0 )

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        #--------------------- DRAWING

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Put a red rectangle somewhere on the surface
        #main_surface.fill((255,0,0), (300, 100, 150, 90))
        paddle.draw(main_surface)

        # Copy our image to the surface, at this (x,y) posn
        main_surface.blit(ball, (100, 120))

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit()


main()