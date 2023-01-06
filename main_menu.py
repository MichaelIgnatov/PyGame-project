import pygame
from functions import terminate, place_text
from button import Button
from load_image import load_image


def main_menu(screen, WIDTH, HEIGHT, clock, FPS):
    file = open("data/result.txt", "r", encoding='utf8')
    text = file.read().strip().split()
    text = 'Всего монет собрано: ' + str(int(text[0]) + int(text[1]) + int(text[2]))
    file.close()

    fon = pygame.transform.scale(load_image('BackgroundFon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    place_text(screen, text, 100, 100)

    image1 = load_image('level1.png')
    image2 = load_image('level2.png')
    image3 = load_image('level3.png')

    level1_button = Button(image1, (340, 200), 'level1.txt')
    level2_button = Button(image2, (355, 300), 'level2.txt')
    level3_button = Button(image3, (355, 400), 'level3.txt')

    menu_running = True
    while menu_running:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(fon, (0, 0))

        level1_button.update(screen)
        level2_button.update(screen)
        level3_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_button.checkForInput(mouse_pos):
                    level = level1_button.checkForInput(mouse_pos)
                    menu_running = False
                if level2_button.checkForInput(mouse_pos):
                    if int(text[0][-1]) > 0:
                        level = level2_button.checkForInput(mouse_pos)
                        menu_running = False
                    else:
                        text = 'Вы собрали недостаточное количество монет'
                        place_text(screen, text, 100, 200)
                if level3_button.checkForInput(mouse_pos):
                    if int(text[0][-1]) > 0:
                        level = level3_button.checkForInput(mouse_pos)
                        menu_running = False
                    else:
                        text = 'Вы собрали недостаточное количество монет'
                        place_text(screen, text, 100, 200)

        pygame.display.flip()
        clock.tick(FPS)
    return level