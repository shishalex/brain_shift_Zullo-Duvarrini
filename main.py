import pygame
import sys
import config
import generator
import ui
from scoring import apply_answer
import random
import time

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")

# Stati del gioco
STATE_START = "start"
STATE_PLAYING = "playing"
STATE_GAMEOVER = "gameover"
game_state = STATE_START

# Variabili di gioco
score = 0
correct_answers = 0
wrong_answers = 0
meter = 0
multiplier = 1

# Generatore random casuale
rng = random.Random()
current_trial = generator.generate_trial(rng)

clock = pygame.time.Clock()

# Variabili per il feedback visivo (colore carta al tasto premuto)
feedback_color = None
feedback_until = 0.0
feedback_trial = None

# --- MAIN LOOP ---
running = True

while running:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Uscita immediata con ESC
            if event.key == pygame.K_ESCAPE:
                running = False

            # Logica SCHERMATA INIZIALE
            if game_state == STATE_START:
                if event.key == pygame.K_SPACE:
                    # Sincronizziamo il tempo di inizio al momento della pressione
                    config.start_time = time.time()
                    game_state = STATE_PLAYING

            # Logica DURANTE IL GIOCO
            elif game_state == STATE_PLAYING:
                if current_time > feedback_until:
                    is_correct = None

                    if event.key == pygame.K_LEFT:
                        is_correct = (current_trial.expected_answer == False)
                    elif event.key == pygame.K_RIGHT:
                        is_correct = (current_trial.expected_answer == True)

                    if is_correct is not None:
                        # Imposta feedback visivo
                        feedback_color = config.CORRECT_CARD_COLOR if is_correct else config.WRONG_CARD_COLOR
                        feedback_until = current_time + 0.2  # Durata feedback
                        feedback_trial = current_trial

                        # Aggiorna statistiche e punteggio
                        if is_correct:
                            correct_answers += 1
                            meter += 1
                            if meter > 3:
                                meter = 0
                                multiplier = min(multiplier + 1, 10)
                        else:
                            wrong_answers += 1
                            if meter > 0:
                                meter = 0
                                multiplier = max(multiplier - 1, 1)

                        score = apply_answer(score, is_correct, multiplier)
                        current_trial = generator.generate_trial(rng)

    # --- DISEGNO ---
    screen.fill((235, 250, 255))

    if game_state == STATE_START:
        ui.draw_game_start(screen)

    elif game_state == STATE_PLAYING:
        remaining = config.time_remaining(config.start_time, config.COUNTDOWN)
        expired = config.is_expired(config.start_time, config.COUNTDOWN)

        if expired:
            # Richiama la funzione passando lo score corrente
            score += 40 * multiplier
            game_state = STATE_GAMEOVER
        else:
            # Disegna la carta e le domande (hints) permanentemente
            if current_time < feedback_until:
                ui.draw_card(screen, feedback_trial, feedback_color)
                if correct_answers < 10:
                    ui.draw_hint(screen, feedback_trial)
            else:
                ui.draw_card(screen, current_trial)
                if correct_answers < 10:
                    ui.draw_hint(screen, current_trial)

            # Interfaccia HUD
            ui.draw_timer_bar(screen, remaining, config.COUNTDOWN)
            ui.draw_timer_text(screen, remaining, expired)
            ui.draw_score(screen, score)
            ui.draw_meter_bar(screen, meter, multiplier)
            ui.draw_answers(screen, correct_answers, wrong_answers)

    elif game_state == STATE_GAMEOVER:
        ui.draw_game_over(screen, score)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()