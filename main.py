import pygame
import sys
import config
from ui import draw_card
from models import Trial

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")

current_trial = Trial(
    letter="A",
    number=7,
    position="TOP",
    expected_answer=True
)

clock = pygame.time.Clock()

# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    draw_card(screen, current_trial, config)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
