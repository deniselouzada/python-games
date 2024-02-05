import pygame
import random

# initialize pygame
pygame.init()

# configure screen
width, height = 600, 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake by @deniselouzada")

#set constants
fps = 3
bg_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = 20
faux_grid = [i for i in range(0, width - size, size)]

# snake and snack definition
snake = pygame.Rect(300, 300, size, size)
snack = pygame.Rect(random.choice(faux_grid), random.choice(faux_grid), size, size)

# functions
def move_snake(dx, dy):
    keys_pressed = pygame.key.get_pressed()
        
    if keys_pressed[pygame.K_LEFT] and dx != size:
        dx = -size
        dy = 0
    if keys_pressed[pygame.K_RIGHT] and dx != -size:
        dx = size
        dy = 0
    if keys_pressed[pygame.K_UP] and dy != size:
        dx = 0
        dy = -size
    if keys_pressed[pygame.K_DOWN] and dy != -size:
        dx = 0
        dy = size
        
    snake.y += dy
    snake.x += dx
    return snake.x, snake.y, dx, dy

def edge_collision():
    if snake.x < 0:
        snake.x = width
    if snake.x > width - size:
        snake.x = 0
    if snake.y < 0:
        snake.y = height
    if snake.y > height - size:
        snake.y = 0
    return snake.x, snake.y

# game over function

def game_over():
    pass

def scoring(score):
    if snake.colliderect(snack):
        snack.x = random.choice(faux_grid)
        snack.y = random.choice(faux_grid)
        score += 1
    font = pygame.font.Font(None, 36)
    text= font.render(f"Score: {score}", 1, white)
    return text, score

# draw on screen
def draw(text):
    screen.fill(bg_color)
    pygame.draw.rect(screen, white, snake)
    pygame.draw.rect(screen, red, snack)
    screen.blit(text, (width / 2 - 250, 20))
    pygame.display.update()

# main loop
def main():
    
    dx = size
    dy = 0
    
    snake.x = random.choice(faux_grid)
    snake.y = random.choice(faux_grid)
    
    snack.x = random.choice(faux_grid)
    snack.y = random.choice(faux_grid)
    
    score = 0
    
    # set clock
    clock = pygame.time.Clock()
    
    running = True
    
    # game loop
    while running:
        clock.tick(fps)

        snake.x, snake.y, dx, dy = move_snake(dx, dy)
        
        snake.x, snake.y = edge_collision()
        
        text, score = scoring(score)
            
        draw(text)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()