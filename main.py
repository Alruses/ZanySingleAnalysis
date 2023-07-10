import sys, pygame
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

#1. Set up our screen - what we're going to be drawing on
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2. Set up a clock to control the refresh rate of our game
clock = pygame.time.Clock()

color = (3, 86, 252)

#3. Make a main function
def main():
    global screen
    #main game loop - this constantly updates our game
    while True:
        #controls refresh rate of our game
        clock.tick(60)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        #to actually make this show up
        pygame.display.flip()
        screen.fill(color)

if __name__ == '__main__':
    main()