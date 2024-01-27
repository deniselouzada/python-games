import pygame
import os

# initialize pygame
pygame.init()

# configure screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")

# set parameters
bg_color = (255, 255, 255)
fps = 60
spaceship_height = 60
spaceship_width = 60
vel = 5
border = pygame.Rect(width/2 - 5, 0, 10, height)

# load images 
yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height)), 270)

# draw window   
def draw_window(red, yellow):
    screen.fill(bg_color)
    screen.blit(yellow_spaceship, (yellow.x, yellow.y))
    screen.blit(red_spaceship, (red.x, red.y))
    pygame.draw.rect(screen, (0, 0, 0), border)
    pygame.display.update()

# handle movement of spaceships  
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0 : # LEFT
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x: # RIGHT
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0: # UP
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < height: # DOWN
        yellow.y += vel
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > border.x + border.width: # LEFT
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width: # RIGHT
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0: # UP
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height: # DOWN
        red.y += vel
        
        
# main function 
def main():
    red = pygame.Rect(500, 200, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 200, spaceship_width, spaceship_height)
    
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
                        
        # update display    
        draw_window(red, yellow)

    pygame.quit()

if __name__ == '__main__':  
    main()
