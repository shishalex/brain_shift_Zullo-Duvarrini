import pygame
import config
from models import Trial


def draw_card(surface: pygame.Surface, trial: Trial, card_color: tuple = config.CARD_COLOR):
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
    pygame.draw.rect(surface, config.TIMER_BAR_BG_COLOR,
                     pygame.Rect(config.TIMER_BAR_X, config.TIMER_BAR_Y, config.TIMER_BAR_W, config.TIMER_BAR_H),
                     border_radius=6)

    fill_w = bar_fill_width(remaining, duration, config.TIMER_BAR_W)
    if remaining > duration * 0.6:
        color = (80, 200, 80)  # verde
    elif remaining > duration * 0.3:
        color = (220, 200, 80)  # giallo
    else:
        color = (220, 80, 80)
    if fill_w > 0:
        pygame.draw.rect(surface, color,
                         pygame.Rect(config.TIMER_BAR_X, config.TIMER_BAR_Y, fill_w, config.TIMER_BAR_H),
                         border_radius=6)


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
    # Bottone NO (Sinistra)
    wrong_answers_rect = pygame.Rect(config.SCREEN_WIDTH // 2 - config.ANSWERS_WIDTH - 30, config.ANSWERS_Y, config.ANSWERS_WIDTH, config.ANSWERS_HEIGHT)
    pygame.draw.rect(surface, (255, 204, 204), wrong_answers_rect, border_radius=20)  # Sfondo rosso chiaro
    pygame.draw.rect(surface, (230, 50, 50), wrong_answers_rect, 4, border_radius=20)  # Bordo rosso scuro

    wrong_answers_text = config.timer_font.render(f"Sbagliate: {wrong_answers}", True, (230, 50, 50))
    wrong_answers_text_rect = wrong_answers_text.get_rect(center=wrong_answers_rect.center)
    surface.blit(wrong_answers_text, wrong_answers_text_rect)

    # Bottone SI (Destra)
    correct_answers_rect = pygame.Rect(config.SCREEN_WIDTH // 2 + 30, config.ANSWERS_Y, config.ANSWERS_WIDTH, config.ANSWERS_HEIGHT)
    pygame.draw.rect(surface, (204, 255, 204), correct_answers_rect, border_radius=20)  # Sfondo verde chiaro
    pygame.draw.rect(surface, (50, 200, 50), correct_answers_rect, 4, border_radius=20)  # Bordo verde scuro

    correct_answers_text = config.timer_font.render(f"Corrette: {correct_answers}", True, (50, 200, 50))
    correct_answers_text_rect = correct_answers_text.get_rect(center=correct_answers_rect.center)
    surface.blit(correct_answers_text, correct_answers_text_rect)


def draw_game_over(surface, score):
    # Utilizziamo card_font per il messaggio principale (è il font più grande in config)
    end_text = config.card_font.render("TEMPO SCADUTO!", True, config.WRONG_CARD_COLOR)

    # Utilizziamo timer_font per mostrare il punteggio
    score_text = config.timer_font.render(f"Punteggio Finale: {score}", True, config.TEXT_COLOR)

    # Utilizziamo hint_font per le istruzioni di uscita
    esc_text = config.hint_font.render("Premi ESC per uscire", True, config.TEXT_COLOR)

    # Posizionamento basato sulle costanti esistenti in config.py
    surface.blit(end_text, (config.SCREEN_WIDTH // 2 - end_text.get_width() // 2, 250))
    surface.blit(score_text, (config.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 400))
    surface.blit(esc_text, (config.SCREEN_WIDTH // 2 - esc_text.get_width() // 2, 550))


def draw_game_start(surface: pygame.Surface):
    # Sfondo iniziale pulito
    surface.fill((235, 250, 255))

    # Titolo del Gioco
    title_surf = config.card_font.render("BRAIN SHIFT", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 100))
    surface.blit(title_surf, title_rect)

    # Testo avvio
    start_surf = config.timer_font.render("Premi la BARRA SPAZIATRICE per avviare", True, (50, 50, 50))
    start_rect = start_surf.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 20))
    surface.blit(start_surf, start_rect)

    # Istruzioni dei comandi
    inst_surf = config.hint_font.render("Usa la Freccia SINISTRA per NO e la Freccia DESTRA per SI", True,
                                        (100, 100, 100))
    inst_rect = inst_surf.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 80))
    surface.blit(inst_surf, inst_rect)

def draw_meter_bar(surface: pygame.Surface):
    # TODO
    pass