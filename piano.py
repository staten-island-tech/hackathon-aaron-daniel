import pygame
import os

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)  # Gray color for pressed keys
YELLOW = (255, 255, 0)  # Highlight color for pressed key

# Define piano keys
WHITE_KEYS = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
BLACK_KEYS = ['W', 'E', 'T', 'Y', 'U', 'O', 'P']
NOTE_SOUNDS = {
    'A': 'sounds/note_C.wav', 'S': 'sounds/note_D.wav', 'D': 'sounds/note_E.wav',
    'F': 'sounds/note_F.wav', 'G': 'sounds/note_G.wav', 'H': 'sounds/note_A.wav',
    'J': 'sounds/note_B.wav', 'K': 'sounds/note_C_high.wav', 'L': 'sounds/note_D_high.wav',
    'W': 'sounds/note_C_sharp.wav', 'E': 'sounds/note_D_sharp.wav', 'T': 'sounds/note_F_sharp.wav',
    'Y': 'sounds/note_G_sharp.wav', 'U': 'sounds/note_A_sharp.wav', 'O': 'sounds/note_C_high_sharp.wav',
    'P': 'sounds/note_D_high_sharp.wav'
}

# Load sounds
for key, sound_file in NOTE_SOUNDS.items():
    if os.path.exists(sound_file):
        NOTE_SOUNDS[key] = pygame.mixer.Sound(sound_file)
    else:
        NOTE_SOUNDS[key] = None  # Placeholder for non-existent sound files

# Define key dimensions
WHITE_KEY_WIDTH = WIDTH // len(WHITE_KEYS)
BLACK_KEY_WIDTH = WHITE_KEY_WIDTH // 2
BLACK_KEY_HEIGHT = HEIGHT // 2

key_pressed = set()

# Draw the piano keys
def draw_piano(pressed_key=None):
    # Draw white keys
    for i, key in enumerate(WHITE_KEYS):
        rect = pygame.Rect(i * WHITE_KEY_WIDTH, 0, WHITE_KEY_WIDTH, HEIGHT)
        color = WHITE
        if pressed_key == key:
            color = GRAY  # Gray when pressed
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)  # Outline
    
    # Draw black keys
    for i, key in enumerate(BLACK_KEYS):
        black_key_x = (i + 1) * WHITE_KEY_WIDTH - BLACK_KEY_WIDTH // 2
        rect = pygame.Rect(black_key_x, 0, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)
        color = BLACK
        if pressed_key == key:
            color = GRAY  # Gray when pressed
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, WHITE, rect, 2)  # Outline

def play_sound(key):
    if NOTE_SOUNDS.get(key) and key not in key_pressed:
        key_pressed.add(key)
        NOTE_SOUNDS[key].play()

# Main game loop
running = True
pressed_key = None  # Track the last pressed key
while running:
    screen.fill((200, 200, 200))  # Set background color to light gray

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            if key in NOTE_SOUNDS:
                pressed_key = key  # Store the key pressed
                play_sound(key)

        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key).upper()
            if key in NOTE_SOUNDS:
                pressed_key = None  # Reset when key is released

    draw_piano(pressed_key)  # Draw the piano with the pressed key highlighted

    pygame.display.flip()  # Update the screen

pygame.quit()
