import pygame
import sys
import config
import generator
from scoring import apply_answer
from ui import draw_card
import random
from models import Trial

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")

# TODO - Fare fase 8

user_answer = None

score = 0

correct_answers = 0
wrong_answers = 0

rng = random.Random(42)

current_trial = generator.generate_trial(rng)

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

            if event.key == pygame.K_LEFT:
                user_answer = False
                is_correct = user_answer == current_trial.expected_answer
                if is_correct:
                    correct_answers += 1
                else:
                    wrong_answers += 1
                apply_answer(score, is_correct)
                current_trial = generator.generate_trial(rng)

            if event.key == pygame.K_RIGHT:
                user_answer = True
                is_correct = user_answer == current_trial.expected_answer
                if is_correct:
                    correct_answers += 1
                else:
                    wrong_answers += 1
                apply_answer(score, is_correct)
                current_trial = generator.generate_trial(rng)


    screen.fill((119,136,153))
    draw_card(screen, current_trial, config)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
