import asyncio
import sys
import pygame
import field
from food import Food
from scoreboard import Scoreboard
from snake import Snake

# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = field.cell_size_pixels * field.cells_count_x
screen_height = field.cell_size_pixels * field.cells_count_y
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Global Variables
bg_color = pygame.Color('#372F3F')
bg_color2 = pygame.Color('#473F4F')
accent_color = (27, 35, 43)
big_font = pygame.font.Font('freesansbold.ttf', 28)
small_font = pygame.font.Font('freesansbold.ttf', 20)
score_sound = pygame.mixer.Sound("score.ogg")

snake = Snake()
food = Food()
food.x = -2
food.y = -2
scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 250)

START = 0
PLAYING = 1
GAME_OVER = 2

state = START

def update():
    global state

    if state != PLAYING:
        return

    # Detect collision with food.
    if (snake.head.x == food.x and
            snake.head.y == food.y):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.move() != True:
        state = GAME_OVER
        return

def draw_start_text():
    text_surface = small_font.render("PRESS ANY KEY TO START", True, (86, 184, 82))
    rc = text_surface.get_rect()
    rc.center = (field.width_pixels / 2, field.height_pixels * 0.8)
    screen.blit(text_surface, rc)

def draw_field():
    for row in range(field.cells_count_y):
        for col in range(field.cells_count_x):
            if (col + row) % 2 == 0:
                grass_rect = pygame.Rect(col * field.cell_size_pixels, row * field.cell_size_pixels, field.cell_size_pixels, field.cell_size_pixels)
                pygame.draw.rect(screen, bg_color2, grass_rect)

def draw():
    global state

    screen.fill(bg_color)
    draw_field()
    food.draw(screen)
    snake.draw(screen)
    scoreboard.draw(screen, big_font)

    if state == START:
        draw_start_text()

    if state == PLAYING:
        rc = pygame.Rect(0, 0, field.cell_size_pixels * 8, field.cell_size_pixels)

    if state == GAME_OVER:
        text_surface = big_font.render("GAME OVER", True, (226, 74, 82))
        rc = text_surface.get_rect()
        rc.center = (field.width_pixels / 2, field.height_pixels * 0.5)
        screen.blit(text_surface, rc)
        draw_start_text()

def restart():
    global state

    food.refresh()
    snake.reset()
    scoreboard.reset()
    state = PLAYING

async def main():
    global state

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                update()

            if event.type == pygame.KEYDOWN:
                if state == PLAYING:
                    if event.key == pygame.K_UP:
                        snake.up()
                    if event.key == pygame.K_DOWN:
                        snake.down()
                    if event.key == pygame.K_LEFT:
                        snake.left()
                    if event.key == pygame.K_RIGHT:
                        snake.right()
                else:
                    restart()

        # Rendering
        draw()

        pygame.display.flip()
        clock.tick(30)

        await asyncio.sleep(0)

asyncio.run(main())
