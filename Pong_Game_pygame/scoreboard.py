import pygame
import field

class Scoreboard:

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def draw(self, screen, font):
        score_text = str(self.l_score)
        score_surface = font.render(score_text, True, pygame.Color('#B7BFB8'))
        score_x = int(field.width * 0.25)
        score_y = 40
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

        score_text = str(self.r_score)
        score_surface = font.render(score_text, True, pygame.Color('#B7BFB8'))
        score_x = int(field.width * 0.75)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)


