import pygame
import config
from models import Trial


def draw_card(surface: pygame.Surface, trial: Trial):
    y = config.Y_POSITIONS[trial.position]
    x = config.X_CENTER

    rect = pygame.Rect(x, y, config.CARD_WIDTH, config.CARD_HEIGHT)

    pygame.draw.rect(surface, config.CARD_COLOR, rect, border_radius=15)
    pygame.draw.rect(surface, (0, 0, 0), rect, 4, border_radius=15)

    content = f"{trial.letter.upper()} {trial.number}"

    text_surf = config.card_font.render(content, True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)

    surface.blit(text_surf, text_rect)

def draw_timer_bar(surface: pygame.Surface, remaining: float, duration: int):
    pygame.draw.rect(surface, config.TIMER_BAR_BG_COLOR, pygame.Rect(config.TIMER_BAR_X, config.TIMER_BAR_Y, config.TIMER_BAR_W, config.TIMER_BAR_H), border_radius=6)

    fill_w = bar_fill_width(remaining, duration, config.TIMER_BAR_W)
    if remaining > duration * 0.6:
        color = (80, 200, 80)  # verde
    elif remaining > duration * 0.3:
        color = (220, 200, 80)  # giallo
    else:
        color = (220, 80, 80)
    if fill_w > 0:
        pygame.draw.rect(surface, color, pygame.Rect(config.TIMER_BAR_X, config.TIMER_BAR_Y, fill_w, config.TIMER_BAR_H), border_radius=6)

def bar_fill_width(remaining: float, duration: int, bar_width: int) -> int:
    ratio = remaining / duration
    fill_w = int(ratio * bar_width)

    return max(0, min(fill_w, bar_width))

def draw_timer_text(surface: pygame.Surface, remaining: float, expired: bool):
    if expired:
        text = "Tempo scaduto!"
        color = (139, 26, 26)
    else:
        text = str(int(remaining))
        color = (0, 0, 0)

    surf = config.timer_font.render(text, True, color)
    y = config.TIMER_BAR_Y + config.TIMER_BAR_H + 10
    rect = surf.get_rect(centerx=config.SCREEN_WIDTH // 2, top=y)
    surface.blit(surf, rect)


def draw_score(surface: pygame.Surface, score: int):
    score_rect = pygame.Rect(config.SCORE_BAR_X, config.SCORE_BAR_Y, config.SCORE_BAR_W, config.SCORE_BAR_H)
    pygame.draw.rect(surface, (173, 216, 230), score_rect, border_radius=10)
    pygame.draw.rect(surface, (0, 0, 0), score_rect, 2, border_radius=10)

    text_surf = config.score_font.render(f"Punti: {score}", True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=score_rect.center)
    surface.blit(text_surf, text_rect)


def draw_answers(surface: pygame.Surface, correct_answers: int, wrong_answers: int):
    # TODO
    pass

def draw_game_over(surface: pygame.Surface):
    # TODO
    pass

def draw_game_start(surface: pygame.Surface):
    # TODO - Fare finestra di avvio del gioco:
    #        La finestra mostra "premi barra spaziatrice per avviare"
    #        Quando si avvia e game_started è True appare tutto il resto (Questo nel main)
    pass