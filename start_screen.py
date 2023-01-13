import pygame
from functions import terminate, place_text
from load_image import load_image


def start_screen(screen, WIDTH, HEIGHT, clock, FPS):  # Стартовый экран
    intro_text = 'Для продолжения нажмите ПКМ или ЛКМ'
    start_sound = pygame.mixer.Sound("data/sounds/start_sound.ogg")
    start_sound.set_volume(0.5)

    fon = pygame.transform.scale(load_image('startfon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    place_text(screen, intro_text, 100, 500)
    start_sound.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)