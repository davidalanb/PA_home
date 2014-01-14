import pygame
import time
import math

class Ball:

    def __init__(self,x,y):
        ball = pygame.image.load("ball.png")
        self.img = pygame.transform.scale( ball, (50,50) )
        self.rect = pygame.Rect(x, y, 50, 50)
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.paused = False

        self.vel = 1
        theta = 45*math.pi/180
        self.vx = self.vel * math.cos(theta)
        self.vy = self.vel * math.sin(theta)

    def update(self, target_surface):

        if not self.paused:
            self.x += self.vx
            self.y += self.vy

        self.rect = pygame.Rect(self.x, self.y, 50, 50)

        w, h = target_surface.get_size()
        print(w,h, self.x, self.y)

        if self.x < 0 or self.x > w-self.w:
            self.vx *= -1
        if self.y < 0:
            self.vy *= -1
        if self.y > h-self.h:
            self.y = 0
            self.paused = True

    def draw(self, target_surface):
        target_surface.fill((255,0,0), self.rect)
        target_surface.blit(self.img, (self.x, self.y))

class Paddle:

    def __init__(self, x, y):
        #self.pos = (x, y)
        self.x = x
        self.y = y

        self.rect = pygame.Rect(x,y,150,25)

    #
    def draw(self, target_surface):
        target_surface.fill((0,255,0), self.rect)

    # move paddle by offsets x and y
    def move(self, x, y):
        self.x += x
        self.y += y

        self.rect = self.rect.move(x, y)

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((800, 600))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    #ball = pygame.image.load("ball.png")
    #ball = pygame.transform.scale( ball, (50,50) )

    paddle = Paddle( 375, 550 )
    ball = Ball( 100, 120 )

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:

        #----------------------- EVENT POLLING ----------------

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            print(key)
            if key == 27:                  # On Escape key ...
                break                      #   leave the game loop
            if key == 112:  # pause / play
                ball.paused = not ball.paused

        # discover held down keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move( -2, 0 )
        if keys[pygame.K_RIGHT]:
            paddle.move( 2, 0 )

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Copy our image to the surface, at this (x,y) posn
        #main_surface.blit(ball, (100, 120))
        ball.update(main_surface)
        ball.draw(main_surface)

        paddle.draw( main_surface )


        #-------------- detect collision -------
        if ball.rect.colliderect(paddle.rect):
            ball.vy *= -1


        # Put a red rectangle somewhere on the surface
        # first tuple is (r, g, b, a)
        # second tuple is (x, y, w, h)
        #main_surface.fill((255,0,0), (100, 500, 150, 90))

        #paddle = pygame.Rect(300,100,150,90)
        #main_surface.fill((255,0,0), paddle)
        #pygame.draw.rect( main_surface, (255,0,0), paddle )

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit()


main()