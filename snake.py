import pygame
import random

# initialize pygame
pygame.init()

# configure screen
width, height = 600, 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake by @deniselouzada")

#set global constants
fps = 60
bg_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = 20
faux_grid = [i for i in range(0, width - size, size)]
pygame.time.set_timer(pygame.USEREVENT, 250)

# snake object definition
class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy
        
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_LEFT] and self.dx != size:
            self.dx = -size
            self.dy = 0
        if keys_pressed[pygame.K_RIGHT] and self.dx != -size:
            self.dx = size
            self.dy = 0
        if keys_pressed[pygame.K_UP] and self.dy != size:
            self.dx = 0
            self.dy = -size
        if keys_pressed[pygame.K_DOWN] and self.dy != -size:
            self.dx = 0
            self.dy = size
        snake.rect.x += snake.dx
        snake.rect.y += snake.dy

# snake object definition
class SnakeTail(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy
        
    def update(self):
        pass

# snack object definition        
class Snack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# snake and snack instantiation
snake = SnakeHead(random.choice(faux_grid), random.choice(faux_grid), size, 0)
snake_group = pygame.sprite.Group(snake)

snack = Snack(random.choice(faux_grid), random.choice(faux_grid))

# functions
def edge_collision():
    for sprite in snake_group:
        if sprite.rect.x < 0:
            sprite.rect.x = width - size
        if sprite.rect.x > width - size:
            sprite.rect.x = 0
        if sprite.rect.y < 0:
            sprite.rect.y = height - size
        if sprite.rect.y > height - size:
            sprite.rect.y = 0

def grow_snake():
    last_sprite = snake_group.sprites()[-1]
    if last_sprite.dy > 0:
        square = SnakeTail(last_sprite.rect.x, last_sprite.rect.y - size, last_sprite.dx, last_sprite.dy)
        snake_group.add(square)
    if last_sprite.dy < 0:
        square = SnakeTail(last_sprite.rect.x, last_sprite.rect.y + size, last_sprite.dx, last_sprite.dy)
        snake_group.add(square)
    if last_sprite.dx > 0:
        square = SnakeTail(last_sprite.rect.x - size, last_sprite.rect.y, last_sprite.dx, last_sprite.dy)
        snake_group.add(square)
    if last_sprite.dx < 0:
        square = SnakeTail(last_sprite.rect.x - size, last_sprite.rect.y, last_sprite.dx, last_sprite.dy)
        snake_group.add(square)

# game over

def game_over():
    pass

def scoring(score):
    if pygame.sprite.collide_rect(snake, snack):
        snack.rect.x = random.choice(faux_grid)
        snack.rect.y = random.choice(faux_grid)
        score += 1
        grow_snake()
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", 1, white)
    return text, score

# draw on screen
def draw(text):
    screen.fill(bg_color)
    pygame.draw.rect(screen, red, snack)
    pygame.draw.rect(screen, white, snake) 
    snake_group.draw(screen)
    screen.blit(text, (width / 2 - 250, 20))
    pygame.display.update()

# main loop
def main():
    
    score = 0
    
    # set clock
    clock = pygame.time.Clock()
    
    running = True
    # game loop
    while running:
        clock.tick(fps)  
        edge_collision()
        text, score = scoring(score)    
        draw(text)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                snake_group.update()
                              
    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()