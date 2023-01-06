import pygame
from functions import terminate, place_text
from load_image import load_image
from button import Button


def end_screen(screen, WIDTH, HEIGHT, clock, FPS, game_result):
    pygame.mouse.set_visible(True)
    new_game = False
    file = open("data/result.txt", "r", encoding='utf8')
    file_text = file.read().strip().split()
    file.close()
    lose_text = f'Вы проиграли! Монет собрано: {file_text[-1]}'
    win_text = f'Уровень пройден! Монет собрано: {file_text[-1]}'

    fon = pygame.transform.scale(load_image('BackgroundFon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    menu_image = load_image('Menu.png')
    exit_image = load_image('Exit.png')

    menu_button = Button(menu_image, (340, 200))
    exit_button = Button(exit_image, (355, 300))

    if game_result == 'lose':
        text = lose_text
        x = 55
        y = 100
    else:
        text = win_text
        x = 35
        y = 100
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(fon, (0, 0))

        place_text(screen, text, x, y, 50)
        menu_button.update(screen)
        exit_button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if menu_button.checkForInput(mouse_pos):
                new_game = True
            if exit_button.checkForInput(mouse_pos):
                running = False
        pygame.display.flip()
        clock.tick(FPS)
    return new_game