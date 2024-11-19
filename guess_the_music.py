import pygame
import os
import random
import sys

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Music")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load music files from the 'music' directory
MUSIC_FOLDER = "music"
music_files = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(('.mp3', '.ogg'))]

# Game variables
score = 0
current_track = ""
current_track_name = ""

# Font setup
font = pygame.font.SysFont("Arial", 24)

# Function to draw text on screen
def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Function to play a random music track
def play_random_music():
    global current_track, current_track_name
    if music_files:
        current_track = random.choice(music_files)
        current_track_name = os.path.splitext(current_track)[0]  # Remove extension
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, current_track))
        pygame.mixer.music.play(loops=0, start=0.0)

# Main game loop
running = True
input_text = ""
while running:
    screen.fill(WHITE)

    # Draw score and instructions
    draw_text(f"Score: {score}", 10, 10)
    draw_text("Guess the track name:", 10, 40)
    draw_text(f"Track: {current_track_name if input_text else '???'}", 10, 80)

    # Draw player input box
    pygame.draw.rect(screen, BLACK, (10, 120, 580, 40), 2)
    draw_text(input_text, 20, 125)

    # Draw button hints
    draw_text("Press Enter to submit guess", 10, 170)
    draw_text("Press Q to quit", 10, 200)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key to submit guess
                if input_text.lower() == current_track_name.lower():
                    score += 1
                    draw_text("Correct! +1 Point!", 10, 250, color=(0, 255, 0))
                else:
                    draw_text(f"Wrong! The track was: {current_track_name}", 10, 250, color=(255, 0, 0))
                input_text = ""  # Clear input box after each guess
                pygame.time.delay(1000)  # Pause for 1 second before next track
                play_random_music()  # Play next track
            elif event.key == pygame.K_q:  # Press Q to quit
                running = False
            elif event.key == pygame.K_BACKSPACE:  # Backspace to remove last character
                input_text = input_text[:-1]
            else:
                input_text += event.unicode  # Add typed character to input text

    # Start playing a track if not already playing
    if not pygame.mixer.music.get_busy() and current_track_name == "":
        play_random_music()

    # Update the screen
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
