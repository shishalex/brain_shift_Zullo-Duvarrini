import time
import pygame

pygame.font.init()

# Inizializziamo il countdown
COUNTDOWN = 30
start_time = time.time()

# Definiamo i bordi dello schermo
SCREEN_WIDTH = 1200
SCREEN_HEIGHT= 800

# Costanti Timer Bar
TIMER_BAR_X = 40
TIMER_BAR_Y = 20
TIMER_BAR_W = SCREEN_WIDTH - 250
TIMER_BAR_H = 30
TIMER_BAR_BG_COLOR = ( 80,  40,  40)

# Costanti carta
CARD_WIDTH = 350
CARD_HEIGHT = 220
GAP = 40
CARD_COLOR = (255,255,255)
CORRECT_CARD_COLOR = (50,205,50)
WRONG_CARD_COLOR = (255,99,71)
TEXT_COLOR = (0,0,0)
TOTAL_BLOCK_HEIGHT = (CARD_HEIGHT * 2) + GAP
VERTICAL_START = (SCREEN_HEIGHT - TOTAL_BLOCK_HEIGHT) // 2

Y_TOP = VERTICAL_START
Y_BOTTOM = VERTICAL_START + CARD_HEIGHT + GAP

X_CENTER = (SCREEN_WIDTH - CARD_WIDTH) // 2

Y_POSITIONS = {
    "top": Y_TOP,
    "bottom": Y_BOTTOM
}

# Costanti Box Punteggio
SCORE_BAR_W = 140
SCORE_BAR_H = 40
SCORE_BAR_X = SCREEN_WIDTH - SCORE_BAR_W - 40
SCORE_BAR_Y = 20

# Costanti Box Suggerimenti
HINT_WIDTH = 350
HINT_HEIGHT = 125
HINT_GAP = 30
HINT_BG_COLOR = (255, 255, 255)
HINT_BORDER_COLOR = (0, 0, 0)

# Costanti Box Risposte
ANSWERS_WIDTH = 220
ANSWERS_HEIGHT = 80
ANSWERS_Y = SCREEN_HEIGHT - ANSWERS_HEIGHT - 40

# Font Usati
card_font = pygame.font.SysFont("Comic Sans", 100, bold=True)
score_font = pygame.font.SysFont("Arial", 22, bold=True)
timer_font = pygame.font.SysFont("Roboto", 40, bold=True)
hint_font = pygame.font.SysFont("Comic Sans", 30, bold=False)

#Funzioni Barra timer
def time_elapsed(start: float) -> float:
    return time.time() - start


def time_remaining(start: float, duration: int) -> float:
    return max(0.0, duration - time_elapsed(start))

def is_expired(start: float, duration: int) -> bool:
    if time_elapsed(start) >= duration:
        return True
    else:
        return False
