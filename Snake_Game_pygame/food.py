import pygame
import random
import field

class Food:
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("apple_small.png")
        self.refresh()

    def refresh(self):
        self.x = random.randint(0, field.cells_count_x - 1)
        self.y = random.randint(0, field.cells_count_y - 1)

    def draw(self, screen):
        rect = pygame.Rect(self.x * field.cell_size_pixels, self.y * field.cell_size_pixels, field.cell_size_pixels, field.cell_size_pixels)
        screen.blit(self.image, rect)
