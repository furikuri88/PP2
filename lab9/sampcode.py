
import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Отрисовка треугольника
pygame.draw.polygon(screen, WHITE, [(0, 0), (0, 400), (400, 400)], 0)

# Основной цикл игры
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Обновление экрана
    pygame.display.flip()

# Завершение игры
pygame.quit()
