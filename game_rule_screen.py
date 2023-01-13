import pygame
from functions import terminate, place_text
from button import Button
from load_image import load_image


def game_rules_screen(screen, WIDTH, HEIGHT, clock, FPS):  # Правила игры
    fon = pygame.transform.scale(load_image('BackgroundFon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    text_rules1 = 'Ваша задача - собрать как можно больше монет,'
    text_rules2 = 'для того чтобы разблокировать слюдующий уровень,'
    text_rules3 = 'и при этом не погибнуть, иначе результат не будет засчитан'
    text_d = 'Для движения вправо, нажмите клавишу D'
    text_a = 'Для движения влево, нажмите клавишу A'
    text_space = 'Для прыжка, нажмите клавишу SPACE'

    exit_image = load_image('Exit.png')
    back_image = load_image('Back.png')

    back_button = Button(back_image, (355, 400), 'level1.txt')
    exit_button = Button(exit_image, (355, 500), 'level2.txt')

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(fon, (0, 0))
        place_text(screen, text_rules1, 30, 100, 32)
        place_text(screen, text_rules2, 35, 140, 32)
        place_text(screen, text_rules3, 35, 180, 32)
        place_text(screen, text_d, 30, 220)
        place_text(screen, text_a, 30, 260)
        place_text(screen, text_space, 30, 300)

        back_button.update(screen)
        exit_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    running = False
                if exit_button.checkForInput(mouse_pos):
                    terminate()

        pygame.display.flip()
        clock.tick(FPS)
