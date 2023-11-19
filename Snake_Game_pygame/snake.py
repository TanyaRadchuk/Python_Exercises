import pygame
import field

field_middle_x = field.cells_count_x // 2
field_middle_y = field.cells_count_y // 2

STARTING_POSITIONS = [(field_middle_x, field_middle_y),
                      (field_middle_x - 1, field_middle_y),
                      (field_middle_x - 2, field_middle_y)]
MOVE_DISTANCE = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Segment:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.heading_dir = RIGHT
        self.color = pygame.Color('#B72F3F')
        self.color.a = 50

    def setheading(self, new_heading):
        self.heading_dir = new_heading

    def heading(self):
        return self.heading_dir

    def get_forward_pos(self):
        next_x = self.x
        next_y = self.y

        if self.heading_dir == RIGHT:
            next_x += 1
        if self.heading_dir == LEFT:
            next_x -= 1
        if self.heading_dir == DOWN:
            next_y += 1
        if self.heading_dir == UP:
            next_y -= 1

        return next_x, next_y


    def position(self):
        return self.x, self.y

    def draw(self, screen):
        rect = pygame.Rect(self.x * field.cell_size_pixels, self.y * field.cell_size_pixels, field.cell_size_pixels, field.cell_size_pixels)
        pygame.draw.rect(screen, self.color, rect)

class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.reset()
        self.eye_image = pygame.image.load("eye.png")

    def reset(self):
        self.segments.clear()

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Segment(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        next_head_pos = self.head.get_forward_pos()

        # Detect collision with wall.
        if (next_head_pos[0] >= field.cells_count_x or
                next_head_pos[0] < 0 or
                next_head_pos[1] >= field.cells_count_y or
                next_head_pos[1] < 0):
            return False

        # Detect collision with tail.
        for segment in self.segments[1:]:
            if (self.head.x == segment.x and
                    self.head.y == segment.y):
                return False

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].x
            new_y = self.segments[seg_num - 1].y
            self.segments[seg_num].x = new_x
            self.segments[seg_num].y = new_y

        self.head.x = next_head_pos[0]
        self.head.y = next_head_pos[1]

        return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def draw(self, screen):
        for i in range(0, len(self.segments)):
            self.segments[i].draw(screen)

        rect = pygame.Rect(self.head.x * field.cell_size_pixels, self.head.y * field.cell_size_pixels, field.cell_size_pixels, field.cell_size_pixels)
        screen.blit(self.eye_image, rect)

