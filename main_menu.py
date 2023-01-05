import pygame
from load_image import load_image
from button import Button
from terminate import terminate


def main_menu(screen):
    background_image = pygame.image.load('data\BackgroundFon.png').convert()

    image1 = load_image('level1.png')
    image2 = load_image('level2.png')
    image3 = load_image('level3.png')

    level1_button = Button(image1, (340, 200), 'level1.txt')
    level2_button = Button(image2, (355, 300), 'level2.txt')
    level3_button = Button(image3, (355, 400), 'level3.txt')

    menu_running = True
    while menu_running:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background_image, (0, 0))

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
                    level = level2_button.checkForInput(mouse_pos)
                    menu_running = False
                if level3_button.checkForInput(mouse_pos):
                    level = level3_button.checkForInput(mouse_pos)
                    menu_running = False

        pygame.display.update()
    return level