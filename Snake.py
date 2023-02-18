import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the Snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.body = [(self.x, self.y)]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, GREEN, (x, y, 10, 10))

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - 10)
        self.y = random.randint(0, WINDOW_HEIGHT - 10)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, 10, 10))

# Create the Snake and Food objects
snake = Snake(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
food = Food()

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 10
            elif event.key == pygame.K_LEFT:
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 10
                snake.dy = 0

    # Move the Snake
    snake.move()

    # Check if the Snake eats the Food
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        food = Food()
        snake.body.append(snake.body[-1])

    # Check if the Snake hits the wall
    if snake.x < 0 or snake.x > WINDOW_WIDTH - 10 or snake.y < 0 or snake.y > WINDOW_HEIGHT - 10:
        running = False

    # Check if the Snake hits itself
    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            running = False

    # Draw the game objects
    window.fill(BLACK)
    snake.draw(window)
    food.draw(window)
    pygame.display.update()

    # Set the game speed
    clock.tick(10)

# Clean up the game
pygame.quit()
