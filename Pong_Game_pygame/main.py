import asyncio
import sys
import pygame
import field
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = field.width
screen_height = field.height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Global Variables
bg_color = pygame.Color('#372F3F')
bg_color2 = pygame.Color('#473F4F')
accent_color = (27, 35, 43)
big_font = pygame.font.Font('freesansbold.ttf', 36)
small_font = pygame.font.Font('freesansbold.ttf', 20)

r_paddle = Paddle((field.width - 40, field.height / 2))
l_paddle = Paddle((40, field.height / 2))
ball = Ball((field.width / 2, field.height / 2))
scoreboard = Scoreboard()

START = 0
PLAYING = 1
GAME_OVER = 2

state = START

def update():
    global state

    if state != PLAYING:
        return

    ball.move()

    if ball.y > screen_height or ball.y <= 0:
        ball.bounce_y()

    # Detect collision with paddles

    if ball.rect.colliderect(r_paddle.rect) and ball.x_move > 0:
        ball.bounce_x()

    if ball.rect.colliderect(l_paddle.rect) and ball.x_move < 0:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.x > field.width:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.x < 0:
        ball.reset_position()
        scoreboard.r_point()

def restart():
    global state
    state = PLAYING

def draw_start_text():
    text_surface = small_font.render("PRESS ANY KEY TO START", True, (86, 184, 82))
    rc = text_surface.get_rect()
    rc.center = (field.width / 2, field.height * 0.75)
    screen.blit(text_surface, rc)

    text_surface = small_font.render("USE 'Q','A' & 'W','S'", True, (86, 184, 82))
    rc = text_surface.get_rect()
    rc.center = (field.width / 2, field.height * 0.85)
    screen.blit(text_surface, rc)

def draw():
    global state

    screen.fill(bg_color)

    pygame.draw.rect(screen, bg_color2, (field.width * 0.5 - 2, 0, 4, field.height))
    centerRect = pygame.Rect(0, 0, 10, 10)
    centerRect.center = (field.width / 2, field.height / 2)
    pygame.draw.rect(screen, bg_color2, centerRect)

    scoreboard.draw(screen, big_font)
    r_paddle.draw(screen)
    l_paddle.draw(screen)
    ball.draw(screen)

    if(state == START):
        draw_start_text()

async def main():
    global state

    r_up_pressed = False
    r_down_pressed = False
    l_up_pressed = False
    l_down_pressed = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if state == PLAYING:
                    if event.key == pygame.K_q:
                        l_up_pressed = True
                    if event.key == pygame.K_a:
                        l_down_pressed = True
                    if event.key == pygame.K_p:
                        r_up_pressed = True
                    if event.key == pygame.K_l:
                        r_down_pressed = True
                else:
                    restart()

            if event.type == pygame.KEYUP:
                if state == PLAYING:
                    if event.key == pygame.K_q:
                        l_up_pressed = False
                    if event.key == pygame.K_a:
                        l_down_pressed = False
                    if event.key == pygame.K_p:
                        r_up_pressed = False
                    if event.key == pygame.K_l:
                        r_down_pressed = False

        if l_up_pressed:
            l_paddle.go_up()

        if l_down_pressed:
            l_paddle.go_down()

        if r_up_pressed:
            r_paddle.go_up()

        if r_down_pressed:
            r_paddle.go_down()

        update()

        # Rendering
        draw()

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

asyncio.run(main())


