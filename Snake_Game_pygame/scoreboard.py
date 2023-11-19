import pygame
import field

class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 0

    def increase_score(self):
        self.score += 1

    def draw(self, screen, font):
        score_text = str(self.score)
        score_surface = font.render(score_text, True, (80, 236, 82))
        score_x = int(field.width_pixels * 0.5)
        score_y = int(field.cell_size_pixels * 0.5)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        bg_rect = score_rect
        bg_rect = bg_rect.inflate(12, 4)
        pygame.draw.rect(screen, (42, 32, 52), bg_rect)
        screen.blit(score_surface, score_rect)
        pygame.draw.rect(screen, (46, 84, 62), bg_rect, 2)

    def reset(self):
        self.score = 0
