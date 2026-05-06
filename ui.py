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
    text_surf = config.FONT.render(content, True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def draw_timer_bar(surface: pygame.Surface, time_left: float, total_time: float):
    x, y = 40, 20
    width = config.SCREEN_WIDTH - 250
    height = 30

    bg_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, (230, 230, 230), bg_rect, border_radius=10)

    progress = max(0.0, min(float(time_left) / float(total_time), 1.0))

    fill_rect = pygame.Rect(x, y, int(width * progress), height)
    if progress > 0:
        pygame.draw.rect(surface, (144, 238, 144), fill_rect, border_radius=10)

    pygame.draw.rect(surface, (0, 0, 0), bg_rect, 2, border_radius=10)


def draw_score(surface: pygame.Surface, score: int):
    width, height = 140, 40
    x = config.SCREEN_WIDTH - width - 40
    y = 20
    score_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, (173, 216, 230), score_rect, border_radius=10)
    pygame.draw.rect(surface, (0, 0, 0), score_rect, 2, border_radius=10)

    font_score = pygame.font.SysFont("Arial", 22, bold=True)
    text_surf = font_score.render(f"Punti: {score}", True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=score_rect.center)
    surface.blit(text_surf, text_rect)


def draw_response_buttons(surface: pygame.Surface):
    btn_w, btn_h = 180, 80
    btn_y = config.SCREEN_HEIGHT - 110
    spacing = 50
    start_x = (config.SCREEN_WIDTH - (btn_w * 2 + spacing)) // 2

    pygame.draw.rect(surface, (255, 180, 180), (start_x, btn_y, btn_w, btn_h), border_radius=20)
    pygame.draw.rect(surface, (0, 0, 0), (start_x, btn_y, btn_w, btn_h), 3, border_radius=20)

    pygame.draw.rect(surface, (180, 255, 180), (start_x + btn_w + spacing, btn_y, btn_w, btn_h), border_radius=20)
    pygame.draw.rect(surface, (0, 0, 0), (start_x + btn_w + spacing, btn_y, btn_w, btn_h), 3, border_radius=20)
