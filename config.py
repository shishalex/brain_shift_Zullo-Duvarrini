import time

import pygame

pygame.font.init()

COUNTDOWN = 30
start_time = time.time()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT= 800

TIMER_BAR_X = 40
TIMER_BAR_Y = 20
TIMER_BAR_W = SCREEN_WIDTH - 250
TIMER_BAR_H = 30
TIMER_BAR_BG_COLOR = ( 80,  40,  40)

CARD_WIDTH = 350
CARD_HEIGHT = 220
GAP = 40
CARD_COLOR = (255,255,255)
TEXT_COLOR = (0,0,0)

SCORE_BAR_W = 140
SCORE_BAR_H = 40
SCORE_BAR_X = SCREEN_WIDTH - SCORE_BAR_W - 40
SCORE_BAR_Y = 20

card_font = pygame.font.SysFont("Comic Sans", 100, bold=True)
score_font = pygame.font.SysFont("Arial", 22, bold=True)

TOTAL_BLOCK_HEIGHT = (CARD_HEIGHT * 2) + GAP
VERTICAL_START = (SCREEN_HEIGHT - TOTAL_BLOCK_HEIGHT) // 2

Y_TOP = VERTICAL_START
Y_BOTTOM = VERTICAL_START + CARD_HEIGHT + GAP

X_CENTER = (SCREEN_WIDTH - CARD_WIDTH) // 2

Y_POSITIONS = {
    "top": Y_TOP,
    "bottom": Y_BOTTOM
}

def time_elapsed(start: float) -> float:
    return time.time() - start


def time_remaining(start: float, duration: int) -> float:
    return max(0.0, duration - time_elapsed(start))

def is_expired(start: float, duration: int) -> bool:
    if time_elapsed(start) >= duration:
        return True
    else:
        return False
