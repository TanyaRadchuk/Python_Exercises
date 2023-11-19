import pygame
import field

class Paddle:
    def __init__(self, position):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.width = 20
        self.height = 80
        self.color = pygame.Color('#B72F3F')
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def go_up(self):
        self.y -= 5

        min_y = self.height / 2

        if self.y <= min_y:
            self.y = min_y

        self.rect.center = (self.x, self.y)

    def go_down(self):
        self.y += 5

        max_y = field.height - self.height / 2

        if self.y >= max_y:
            self.y = max_y

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

