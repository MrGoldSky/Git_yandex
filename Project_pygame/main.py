#---Импорт библиотек---
import pygame
import time
from time import strftime, gmtime
from random import randint
import sqlite3

#---Константы---
WIDTH = 500
HEIGHT = 500

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
collor_score = pygame.Color(65, 105, 225)
collor_snake = pygame.Color(3, 192, 60)
collor_apple = pygame.Color(196, 48, 43)

snake_speed = 7
snake_position = [100, 50]

snake = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
    ]

apple = []
apple_spawn = True
apple_count = 1

last_direction = "DOWN"
now_direction = last_direction

score = 0
game_run = False


#---Подключение к базе данных---
def connect_to_db():
    try:
        con = sqlite3.connect("Git_yandex/Project_pygame/base/db.sqlite")
        cur = con.cursor()
        return con, cur
    except BaseException as e:
        print()
        print("Ошибка подключения к БД")
        print(e)


#---Создание новой игры, стартовое окно---
def new_game():
    try:
        global game_run
        game_over_font = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 20)
        game_over_surface = game_over_font.render(
            "Нажмите ENTER, чтобы начать", True, pygame.Color(255, 255, 255)
        )
        game_over_screen = game_over_surface.get_rect()
        game_over_screen.midtop = (WIDTH / 2, HEIGHT / 4)
        screen.blit(game_over_surface, game_over_screen)
        pygame.display.flip()

        while not game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_run = True
                        apple_generate()
    except BaseException as e:
        print()
        print("Ошибка начала игры")
        print(e)


#---Показ лучшего результата---
def update_record():
    try:
        con, cur = connect_to_db()
        record = cur.execute(f"""SELECT max(result) from pygame
                             """).fetchone()[0]
        record_score_font_style = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 35)
        record_score_surface = record_score_font_style.render(f"Максимум очков {record}", True, black)
        record_score_coordinates = [record_score_surface.get_rect()[0] + 254, record_score_surface.get_rect()[1]]
        screen.blit(record_score_surface, record_score_coordinates)
    except BaseException as e:
        print()
        print("Ошибка показа лучшего результата")
        print(e)


#---Обновление очков---
def update_score():
    try:
        score_font_style = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 35)
        score_surface = score_font_style.render(f"Вы набрали {score} очков", True, black)
        score_rectangle = score_surface.get_rect()
        screen.blit(score_surface, score_rectangle)
    except BaseException as e:
        print()
        print("Ошибка показа очков")
        print(e)


#---Конец игры, финальное окно---
def game_over():
    try:
        game_over_font = pygame.font.SysFont("Git_yandex/Project_pygame/font/NeueMachina-Light.ttf", 50)
        game_over_surface = game_over_font.render(
            f"Вы набрали {score} очков", True, collor_score
        )
        game_over_screen = game_over_surface.get_rect()
        game_over_screen.midtop = (WIDTH / 2, HEIGHT / 4)
        screen.blit(game_over_surface, game_over_screen)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        insert_score(score)
        quit()
    except BaseException as e:
        print()
        print("Ошибка конца игры")
        print(e)


#---Сохранение результатов---
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
    except BaseException as e:
        print()
        print("Ошибка заполнения БД (score, time)")
        print(e)


#---Генерация яблок---
def apple_generate():
    apple.append([
        randint(1, (WIDTH // 10)) * 10,
        randint(1, (HEIGHT // 10)) * 10
        ])


#---Ранер---
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Змейка")
    game_clock = pygame.time.Clock()
    
    new_game()

    try:
        while game_run:

            #---Считывание движения---
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

            #---Движение змеи---
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

            #---Поедание яблок, ускорение змейки, добавление количества яблок---
            add_len = False
            for apple_position in apple:
                if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
                    score += 1
                    apple_spawn = False
                    snake_speed += 0.2
                    apple_count += 1
                    add_len = True
                    del apple[apple.index(apple_position)]
            if not add_len:
                snake.pop()

            if not apple_spawn:
                for count in range(apple_count):
                    apple_generate()
            apple_spawn = True
            screen.fill(white)

            #---Отрисовка змейки---
            for position in snake:
                pygame.draw.rect(screen, collor_snake, pygame.Rect(position[0], position[1], 10, 10))
            
            #---Отрисовка яблок---
            for apple_position in apple:
                pygame.draw.rect(screen, collor_apple, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

            #---Проверка границ---
            if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
                game_over()

            for block in snake[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()

            update_score()
            update_record()

            pygame.display.update()
            game_clock.tick(snake_speed)
    except BaseException as e:
        print()
        print("Ошибка в главном цикле")
        print(e)
    pygame.quit()
