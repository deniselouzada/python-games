import pygame
import random

# initialize pygame
pygame.init()

# configure screen
width, height = 800, 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong with pygame")

# set constants
fps = 60
bg_color = (0, 0, 0)
white = (255, 255, 255)
direction = [1, -1]

# define objects
paddle_a = pygame.Rect(20, 250, 20, 100)
paddle_b = pygame.Rect(760, 250, 20, 100)
ball = pygame.Rect(400, 300, 20, 20)

# main loop
def main():
    
    # initializing speed and direction for the ball
    dx = 2
    dy = 2
    
    # initialize scores
    score_a = 0
    score_b = 0
    
    # set clock
    clock = pygame.time.Clock()
    
    # game loop
    running = True
    while running:
        clock.tick(fps)
        screen.fill(bg_color)
        
        # draw objects
        pygame.draw.rect(screen, white, paddle_a)
        pygame.draw.rect(screen, white, paddle_b)
        pygame.draw.rect(screen, white, ball)
        
        # get keys and handle movement
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
                 
        # paddle ball collisions
        if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
            dx *= -1
            dy *= random.choice(direction)
        
        # scoring
        if ball.x > width:
            ball.x = 400
            ball.y = 300
            score_a += 1
        elif ball.x < 0:
            ball.x = 400
            ball.y = 300
            score_b += 1
        
        # collisions with top and bottom of screen
        elif ball.y > height - ball.height:
            dy *= -1
        elif ball.y < 0:
            dy *= -1
            
        # draw scores
        font = pygame.font.Font(None, 36)
        text_a = font.render(f"Player A: {score_a}", 1, white)
        text_b = font.render(f"Player B: {score_b}", 1, white)
        screen.blit(text_a, (width / 2 - 250, 20))
        screen.blit(text_b, (width / 2 + 100, 20))
        
        # update ball's direction
        ball.x += dx
        ball.y += dy
       
        # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()