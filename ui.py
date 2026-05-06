import pygame
from models import Trial

def draw_card(surface: pygame.Surface, trial: Trial, config):
    x = config.X_CENTER
    y = config.Y_POSITIONS[trial.position]

    rect = pygame.Rect(x, y, config.CARD_WIDTH, config.CARD_HEIGHT)

    pygame.draw.rect(surface, config.CARD_COLOR, rect)
    pygame.draw.rect(surface, config.CARD_COLOR, rect, 3)

    card_text = f"{trial.letter.upper()} {trial.number}"

    text_surf = config.FONT.render(card_text, True, config.TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)