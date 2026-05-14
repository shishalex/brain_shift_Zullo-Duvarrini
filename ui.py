import pygame
import config
from models import Trial


def draw_card(surface: pygame.Surface, trial: Trial, card_color: tuple=config.CARD_COLOR):
    y = config.Y_POSITIONS[trial.position]
    x = config.X_CENTER

    rect = pygame.Rect(x, y, config.CARD_WIDTH, config.CARD_HEIGHT)

    pygame.draw.rect(surface, card_color, rect, border_radius=15)
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


def draw_hint(surface: pygame.Surface, trial: Trial):
    card_y = config.Y_POSITIONS[trial.position]
    card_x = config.X_CENTER
    center_y = card_y + (config.CARD_HEIGHT // 2)

    if trial.position == "top":
        hint_x = card_x + config.CARD_WIDTH + config.HINT_GAP
        hint_y = center_y - (config.HINT_HEIGHT // 2)
        text = "Il numero è pari?"
        arrow_start = (hint_x, center_y)
        arrow_end = (card_x + config.CARD_WIDTH + 8, center_y)

    else:
        hint_x = card_x - config.HINT_WIDTH - config.HINT_GAP
        hint_y = center_y - (config.HINT_HEIGHT // 2)
        text = "La lettera è una vocale?"
        arrow_start = (hint_x + config.HINT_WIDTH, center_y)
        arrow_end = (card_x - 8, center_y)

    hint_rect = pygame.Rect(hint_x, hint_y, config.HINT_WIDTH, config.HINT_HEIGHT)
    pygame.draw.rect(surface, config.HINT_BG_COLOR, hint_rect, border_radius=15)
    pygame.draw.rect(surface, config.HINT_BORDER_COLOR, hint_rect, 3, border_radius=15)

    text_surf = config.hint_font.render(text, True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=hint_rect.center)
    surface.blit(text_surf, text_rect)

    pygame.draw.line(surface, config.HINT_BORDER_COLOR, arrow_start, arrow_end, 3)

    if trial.position == "top":
        point1 = (arrow_end[0] + 10, arrow_end[1] - 8)
        point2 = (arrow_end[0] + 10, arrow_end[1] + 8)
    else:
        point1 = (arrow_end[0] - 10, arrow_end[1] - 8)
        point2 = (arrow_end[0] - 10, arrow_end[1] + 8)

    pygame.draw.polygon(surface, config.HINT_BORDER_COLOR, [arrow_end, point1, point2])


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