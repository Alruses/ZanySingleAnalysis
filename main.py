import sys, pygame, random
from pygame.locals import *


pygame.init()
screen_info = pygame.display.Info()

#1. Set up our screen - what we're going to be drawing on
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2. Set up a clock to control the refresh rate of our game
clock = pygame.time.Clock()

color = (3, 86, 232)

#load image of a fish
fish_image = pygame.image.load("fishy.png")
fish_image = pygame.transform.smoothscale(fish_image, (50,75))
fish_rect = fish_image.get_rect()

fish_rect.center = (width//2, height//2)

speed = pygame.math.Vector2(5,5)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, rotation)

def move_fish():
    global fish_image
    fish_rect.move_ip(speed)

    #check if we've gone past the walls of the screen
    if fish_rect.left < 0 or fish_rect.right > screen_info.current_w:
        #reversing the x speed, which is index 0 of our speed variable
        speed[0] *= -1
        fish_image = pygame.transform.flip(fish_image, True, False)
        #making it move a little away from the wall so it doesn't get stuck in the wall and flip over and over
        fish_rect.move_ip(speed[0],0)
        
    if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
        #reversing the x speed, which is index 0 of our speed variable
        speed[1] *= -1
        fish_image = pygame.transform.flip(fish_image, False, True)
        #making it move a little away from the wall so it doesn't get stuck in the wall and flip over and over
        fish_rect.move_ip(0, speed[1])
    
    
    


#3. Make a main function
def main():
    global screen
    #main game loop - this constantly updates our game
    while True:
        #controls refresh rate of our game
        clock.tick(60)
        move_fish()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        #to actually make this show up
        screen.fill(color)
        screen.blit(fish_image, fish_rect)
        pygame.display.flip()
       

if __name__ == '__main__':
    main()