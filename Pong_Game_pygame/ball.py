import pygame
import field

class Ball:

    def __init__(self, position):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 0.1
        self.color = pygame.Color('#B7BFB8')
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        self.rect.center = (self.x, self.y)

    def move(self):
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.x = field.width / 2
        self.y = field.height / 2
        self.move_speed = 0.1
        self.bounce_x()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.rect.width / 2)

