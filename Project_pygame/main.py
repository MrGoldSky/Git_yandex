import pygame
import time
from time import strftime, gmtime
from random import randrange
import sqlite3

WIDTH = 500
HEIGHT = 500

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
collor_score = pygame.Color(220, 20, 60)
collor_snake = pygame.Color(124, 252, 0)
collor_apple = pygame.Color(255, 0, 0)

snake_speed = 10
snake_position = [100, 50]

snake = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
    ]

apple_position = [
    randrange(1, (WIDTH // 10)) * 10,
    randrange(1, (HEIGHT // 10)) * 10
    ]
apple_spawn = True

last_direction = "DOWN"
now_direction = last_direction

score = 0
game_run = False


def new_game():
    try:
        global game_run
        game_over_font = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 20)
        game_over_surface = game_over_font.render(
            "Нажмите ENTER, чтобы начать", True, pygame.Color(255, 255, 255)
        )
        game_over_screen = game_over_surface.get_rect()
        game_over_screen.midtop = (WIDTH / 2, HEIGHT / 4)
        display_screen.blit(game_over_surface, game_over_screen)
        pygame.display.flip()

        while not game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_run = True
    except BaseException as e:
        print("Ошибка начала игры")
        print(e)


def display_score():  
    score_font_style = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 35)
    score_surface = score_font_style.render("Очки: " + str(score), True, black)
    score_rectangle = score_surface.get_rect()
    display_screen.blit(score_surface, score_rectangle)


def game_over():
    game_over_font = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 50)
    game_over_surface = game_over_font.render(
        "Очки: " + str(score), True, collor_score
    )
    game_over_screen = game_over_surface.get_rect()
    game_over_screen.midtop = (WIDTH / 2, HEIGHT / 4)
    display_screen.blit(game_over_surface, game_over_screen)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    insert_score(score)
    quit()


def connect_to_db():
    try:
        con = sqlite3.connect("Git_yandex/Project_pygame/base/db.sqlite")
        cur = con.cursor()
        return con, cur
    except BaseException as e:
        print("Ошибка подключения к БД")
        print(e)


def insert_score(score):
    con, cur = connect_to_db()
    try:
        result = cur.execute(f"""INSERT 
                             INTO pygame(result, time) 
                             VALUES({int(score)},'{strftime("%Y-%m-%d %H:%M:%S", gmtime())}')
                             """)
        con.commit()
        con.close()
        return result
    except BaseException as exception:
        print("Ошибка заполнения БД (score, time)")
        print(exception)


if __name__ == "__main__":
    pygame.init()
    display_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Змейка")
    game_clock = pygame.time.Clock()

    new_game()

    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    now_direction = "UP"
                if event.key == pygame.K_DOWN:
                    now_direction = "DOWN"
                if event.key == pygame.K_LEFT:
                    now_direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    now_direction = "RIGHT"

        if now_direction == "UP" and last_direction != "DOWN":
            last_direction = "UP"
        if now_direction == "DOWN" and last_direction != "UP":
            last_direction = "DOWN"
        if now_direction == "LEFT" and last_direction != "RIGHT":
            last_direction = "LEFT"
        if now_direction == "RIGHT" and last_direction != "LEFT":
            last_direction = "RIGHT"

        if last_direction == "UP":
            snake_position[1] -= 10
        if last_direction == "DOWN":
            snake_position[1] += 10
        if last_direction == "LEFT":
            snake_position[0] -= 10
        if last_direction == "RIGHT":
            snake_position[0] += 10

        snake.insert(0, list(snake_position))
        if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
            score += 1
            apple_spawn = False
            snake_speed += 0.2
        else:
            snake.pop()

        if not apple_spawn:
            apple_position = [
                randrange(1, (WIDTH // 10)) * 10,
                randrange(1, (HEIGHT // 10)) * 10
            ]
        apple_spawn = True
        display_screen.fill(white)

        for position in snake:
            pygame.draw.rect(display_screen, collor_snake, pygame.Rect(position[0], position[1], 10, 10))
            pygame.draw.rect(display_screen, collor_apple, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
            game_over()

        for block in snake[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        display_score()
        pygame.display.update()
        game_clock.tick(snake_speed)
    
    pygame.quit()
