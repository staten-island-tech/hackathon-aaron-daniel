import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SIZE = 50  # Player character size
PUNCH_RANGE = 80  # How far the punch extends

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shadow Boxing Game")

# Define Player class
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.color = RED
        self.speed = 5
        self.punching = False
        self.punch_direction = 'NONE'

    def move(self, dx, dy):
        """Move the player around the screen"""
        if 0 <= self.x + dx <= SCREEN_WIDTH - self.width:
            self.x += dx
        if 0 <= self.y + dy <= SCREEN_HEIGHT - self.height:
            self.y += dy

    def punch(self, direction):
        """Set the punching direction"""
        self.punching = True
        self.punch_direction = direction

    def draw(self, surface):
        """Draw the player"""
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        # Draw punch animation (only when punching)
        if self.punching:
            punch_color = BLACK
            if self.punch_direction == 'UP':
                pygame.draw.line(surface, punch_color, (self.x + self.width // 2, self.y), (self.x + self.width // 2, self.y - PUNCH_RANGE), 5)
            elif self.punch_direction == 'DOWN':
                pygame.draw.line(surface, punch_color, (self.x + self.width // 2, self.y + self.height), (self.x + self.width // 2, self.y + self.height + PUNCH_RANGE), 5)
            elif self.punch_direction == 'LEFT':
                pygame.draw.line(surface, punch_color, (self.x, self.y + self.height // 2), (self.x - PUNCH_RANGE, self.y + self.height // 2), 5)
            elif self.punch_direction == 'RIGHT':
                pygame.draw.line(surface, punch_color, (self.x + self.width, self.y + self.height // 2), (self.x + self.width + PUNCH_RANGE, self.y + self.height // 2), 5)

            # Reset the punch after a brief time
            self.punching = False
            self.punch_direction = 'NONE'

# Initialize the player
player = Player()

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key handling
        keys = pygame.key.get_pressed()

        # Player movement (WASD or arrow keys)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move(-player.speed, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move(player.speed, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move(0, -player.speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move(0, player.speed)

        # Player punching (spacebar or directional keys)
        if keys[pygame.K_SPACE]:
            player.punch('UP')
        elif keys[pygame.K_DOWN]:
            player.punch('DOWN')
        elif keys[pygame.K_LEFT]:
            player.punch('LEFT')
        elif keys[pygame.K_RIGHT]:
            player.punch('RIGHT')

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game loop
game_loop()
