import pygame

icon = pygame.image.load('assets/icon.png') # подгрузка картинки 32х32 (для начала ее нужно скачать)
blue_bg = (0, 0, 255) # синий цвет (для заднего фона)

pygame.init() # инициализация библиотеки

screen = pygame.display.set_mode((800, 600)) # создание окна определенного размера
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) - или полноэкранный режим
pygame.display.set_caption('Писька бобра') # заголовок окна
pygame.display.set_icon(icon) # задаем иконку окна (слева от заголовка)

gameStarted = True # состояние игры (запущена)
while gameStarted: # главный цикл (пока игра запущена)
    # === 1. Главный цикл игры ===
    for event in pygame.event.get(): # считываем все события, во время работы игры
        if event.type == pygame.QUIT: # если событие - выход из игры (кнопка закрытия окна)
            gameStarted = False # останавливаем игру

    # === 2. Основная логика игры ===
        # просчеты движения
        # просчеты физики

    # === 3. Отрисовка всех элементов, обновление ===
    screen.fill(blue_bg) # заливка окна цветом
    pygame.display.flip() # обновление экрана

pygame.quit() # завершение работы библиотеки (очистка памяти)
