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
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy
        
    def grow(self):
        self.image.fill(white)
        self.rect = self.image.get_rect()
        
    def update(self):
        pass
        

class Snack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# snake and snack instantiation
snake = Snake(random.choice(faux_grid), random.choice(faux_grid), size, 0)
snake_group = pygame.sprite.Group()

snack = Snack(random.choice(faux_grid), random.choice(faux_grid))

# functions
def move_snake():
    keys_pressed = pygame.key.get_pressed()
        
    if keys_pressed[pygame.K_LEFT] and snake.dx != size:
        snake.dx = -size
        snake.dy = 0
    if keys_pressed[pygame.K_RIGHT] and snake.dx != -size:
        snake.dx = size
        snake.dy = 0
    if keys_pressed[pygame.K_UP] and snake.dy != size:
        snake.dx = 0
        snake.dy = -size
    if keys_pressed[pygame.K_DOWN] and snake.dy != -size:
        snake.dx = 0
        snake.dy = size
        
    snake.rect.y += snake.dy
    snake.rect.x += snake.dx
    return snake.rect.x, snake.rect.y, snake.dx, snake.dy

def edge_collision():
    if snake.rect.x < 0:
        snake.rect.x = width - size
    if snake.rect.x > width - size:
        snake.rect.x = 0
    if snake.rect.y < 0:
        snake.rect.y = height - size
    if snake.rect.y > height - size:
        snake.rect.y = 0
    return snake.rect.x, snake.rect.y

def grow_snake():
    pass

# game over

def game_over():
    pass

def scoring(score):
    if pygame.sprite.collide_rect(snake, snack):
        snack.rect.x = random.choice(faux_grid)
        snack.rect.y = random.choice(faux_grid)
        score += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", 1, white)
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
    
    #snake_group.draw(screen)
    
    score = 0
    
    # set clock
    clock = pygame.time.Clock()
    
    running = True
    
    # game loop
    while running:
        clock.tick(fps)

        snake.rect.x, snake.rect.y, snake.dx, snake.dy = move_snake()
        
        snake.rect.x, snake.rect.y = edge_collision()
        
        text, score = scoring(score)
            
        draw(text)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()