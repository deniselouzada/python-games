import pygame
import random

# initialize pygame
pygame.init()

# configure screen
width, height = 800, 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#set constants
fps = 60
bg_color = (0, 0, 0)
white = (255, 255, 255)
direction = [1, -1]

# Define objects

paddle_a = pygame.Rect(20, 250, 20, 100)

paddle_b = pygame.Rect(760, 250, 20, 100)

ball = pygame.Rect(400, 300, 20, 20)

# main loop
def main():
    
    dx = 1
    dy = 1
    
    # set clock
    clock = pygame.time.Clock()
    
    # game loop
    running = True
    while running:
        clock.tick(fps)
        screen.fill(bg_color)
        
        pygame.draw.rect(screen, white, paddle_a)
        pygame.draw.rect(screen, white, paddle_b)
        pygame.draw.rect(screen, white, ball)
                
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_ESCAPE]:
            running = False
        elif keys_pressed[pygame.K_s] and paddle_a.y < height - paddle_a.height:
            paddle_a.y += 5
        elif keys_pressed[pygame.K_w] and paddle_a.y > 0:
            paddle_a.y -= 5
        elif keys_pressed[pygame.K_DOWN] and paddle_b.y < height - paddle_b.height:
            paddle_b.y += 5
        elif keys_pressed[pygame.K_UP] and paddle_b.y > 0:
            paddle_b.y -= 5
            
        
        
        if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
            dx *= -1
            dy *= -1
        
        if ball.x > width:
            ball.x = 400
            ball.y = 300
        elif ball.x < 0:
            ball.x = 400
            ball.y = 300
        elif ball.y > height - ball.height:
            dy *= -1
        elif ball.y < 0:
            dy *= -1
        
        ball.x += dx
        ball.y += dy
       
        # event handling

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()