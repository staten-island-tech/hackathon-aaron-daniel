import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ARROW_SPEED = 5  # Speed of arrow movement
ARROW_SIZE = 50  # Size of the arrows
MARGIN = 100  # Space from the bottom where arrows appear
KEYS = ['LEFT', 'DOWN', 'UP', 'RIGHT']  # Direction keys

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Friday Night Funkin\'-like Game')

# Font
font = pygame.font.Font(None, 36)

# Arrow class
class Arrow:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
        self.color = LIGHT_BLUE
        self.key = direction

    def move(self):
        self.y += ARROW_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, ARROW_SIZE, ARROW_SIZE))
        text = font.render(self.key, True, WHITE)
        surface.blit(text, (self.x + ARROW_SIZE // 4, self.y + ARROW_SIZE // 4))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    arrows = []
    score = 0
    running = True
    last_arrow_time = time.time()
    pressed_keys = set()  # To track pressed keys

    while running:
        screen.fill((0, 0, 0))  # Background color

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pressed_keys.add('LEFT')
                elif event.key == pygame.K_DOWN:
                    pressed_keys.add('DOWN')
                elif event.key == pygame.K_UP:
                    pressed_keys.add('UP')
                elif event.key == pygame.K_RIGHT:
                    pressed_keys.add('RIGHT')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_keys.discard('LEFT')
                elif event.key == pygame.K_DOWN:
                    pressed_keys.discard('DOWN')
                elif event.key == pygame.K_UP:
                    pressed_keys.discard('UP')
                elif event.key == pygame.K_RIGHT:
                    pressed_keys.discard('RIGHT')

        # Generate arrows at regular intervals
        if time.time() - last_arrow_time > 1:  # Generate an arrow every 1 second
            last_arrow_time = time.time()
            direction = random.choice(KEYS)
            x_pos = SCREEN_WIDTH // 2 - ARROW_SIZE // 2
            arrows.append(Arrow(direction, x_pos, MARGIN))
        
        # Move arrows and check for input
        for arrow in arrows[:]:
            arrow.move()
            if arrow.y > SCREEN_HEIGHT:
                arrows.remove(arrow)
            elif arrow.y > SCREEN_HEIGHT - 100 and arrow.key in pressed_keys:
                score += 10
                arrows.remove(arrow)

            arrow.draw(screen)

        # Display score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the game loop
game_loop()
