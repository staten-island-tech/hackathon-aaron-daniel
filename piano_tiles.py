import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Infinite Piano Tiles')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font for score
font = pygame.font.SysFont('Arial', 30)

# Tile properties
TILE_WIDTH = WIDTH // 4
TILE_HEIGHT = 100
TILE_SPEED = 5  # Speed of falling tiles

# Game variables
score = 0
game_running = True
tile_list = []

# Define key mappings for A, S, K, L
KEY_MAPPING = {
    pygame.K_a: 0,  # Leftmost column
    pygame.K_s: 1,  # Second column
    pygame.K_k: 2,  # Third column
    pygame.K_l: 3,  # Rightmost column
}

# Function to create new tiles
def create_tile():
    x = random.randint(0, 3) * TILE_WIDTH  # Random x position for the tile
    y = -TILE_HEIGHT  # Start from the top of the screen
    tile_list.append(pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT))

# Function to draw the game screen
def draw_game():
    screen.fill(WHITE)
    
    # Draw tiles
    for tile in tile_list:
        pygame.draw.rect(screen, BLACK, tile)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

# Function to handle tile movements and score
def handle_tiles():
    global score, game_running
    for tile in tile_list:
        tile.y += TILE_SPEED  # Move the tile down

        # Check if the tile reaches the bottom of the screen
        if tile.y >= HEIGHT:
            tile_list.remove(tile)  # Remove the tile if it falls off
            game_running = False  # Game over if a tile falls off

# Main game loop
while game_running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_MAPPING:
                column = KEY_MAPPING[event.key]
                # Check if there's a tile in the pressed column and remove it
                for tile in tile_list:
                    if tile.x // TILE_WIDTH == column and tile.y + TILE_HEIGHT >= HEIGHT - TILE_SPEED:
                        tile_list.remove(tile)  # Remove the clicked tile
                        score += 1  # Increase score
                        break

    # Add a new tile every 1 second
    if random.random() < 0.02:  # Adjust the frequency of new tiles
        create_tile()

    # Handle tile movement and game logic
    handle_tiles()

    # Draw the game screen
    draw_game()

    # Control the frame rate
    pygame.time.Clock().tick(60)  # 60 frames per second

# Game Over
pygame.quit()
print(f"Game Over! Final Score: {score}")
