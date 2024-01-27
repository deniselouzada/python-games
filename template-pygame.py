import pygame

# initialize pygame
pygame.init()

# configure screen
width, height = 640, 480
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#set constants
fps = 60
bg_color = (0, 0, 0)

def draw():
    screen.fill(bg_color)
    pygame.display.update()

# main loop
def main():
    
    #clock = pygame.time.Clock()
    running = True
    while running:
    #    clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #keys_pressed = pygame.key.get_pressed()
        #draw()

    pygame.quit()

if __name__ == "__main__":
    main()