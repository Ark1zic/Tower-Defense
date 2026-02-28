import pygame


WIN_SIZE =[800, 600]
MAX_FPS = 60

win = pygame.Window('Tower Defense', WIN_SIZE)

surface = win.get_surface()
clock = pygame.Clock()

running = True
while running:
# Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False

        # Обновление объектов

        # Отрисовка
    surface.fill("orange")

    win.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())








































