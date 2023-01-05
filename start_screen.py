import pygame
from load_image import load_image
from terminate import terminate


def start_screen(screen, WIDTH, HEIGHT, clock, FPS):
    intro_text = ['Для продолжения нажмите ПКМ или ЛКМ']

    fon = pygame.transform.scale(load_image('startfon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(11, 191, 83))
        intro_rect = string_rendered.get_rect()
        intro_rect.x = 135
        intro_rect.y = 500
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)