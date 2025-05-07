import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# FPS
FPS = 10

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont('arial', 25)

def draw_text(text, color, x, y):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def random_food_position():
    return (
        random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    )

def game_over_screen(score):
    screen.fill(BLACK)
    draw_text(f"Игра окончена! Счёт: {score}", RED, WIDTH // 4, HEIGHT // 3)
    draw_text("Нажмите любую клавишу для выхода...", WHITE, WIDTH // 6, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL_SIZE, 0)
    food = random_food_position()
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
            direction = (0, -CELL_SIZE)
        elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
            direction = (0, CELL_SIZE)
        elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
            direction = (-CELL_SIZE, 0)
        elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
            direction = (CELL_SIZE, 0)

        # Обновление позиции змейки
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Проверка на столкновения
        if (new_head in snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            game_over_screen(score)

        snake.insert(0, new_head)

        # Проверка на еду
        if new_head == food:
            score += 1
            food = random_food_position()
        else:
            snake.pop()

        # Отрисовка
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
        draw_text(f"Счёт: {score}", WHITE, 10, 10)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
