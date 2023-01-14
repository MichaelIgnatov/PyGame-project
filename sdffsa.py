from camera import Camera
from start_screen import start_screen
from functions import load_level, generate_level, terminate
from variables import all_sprites, enemies_group, coins_group, portal_group
from main_menu import main_menu
from end_screen import end_screen
import pygame

pygame.init()
size = WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Cube")
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
clock = pygame.time.Clock()
FPS = 30
new_game = False
menu_condition = True
game_condition = False
end_condition = False

background = pygame.image.load('data\BackgroundFon.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())


def game(screen, WIDTH, HEIGHT, clock, FPS, running):
    while running:
        screen.fill(BLACK)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                player.update(event.key)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.update(pygame.K_w)
        if keys[pygame.K_s]:
            player.update(pygame.K_s)
        if keys[pygame.K_d]:
            player.update(pygame.K_d)
        if keys[pygame.K_a]:
            player.update(pygame.K_a)

        player.health_display(screen)

        enemies_group.update(player)

        coins_group.update(player)

        portal_group.update()

        screen.blit(background, (0, 0))
        camera.update(player, WIDTH, HEIGHT)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        pygame.display.flip()
        if player.death:
            running = False
    screen.fill(BLACK)


start_screen(screen, WIDTH, HEIGHT, clock, FPS)
main_running = True

while main_running:
    if menu_condition:
        pygame.display.flip()
        level = main_menu(screen, WIDTH, HEIGHT, clock, FPS)
        player, level_x, level_y = generate_level(load_level(level))
        player.set_current_level(level)
        camera = Camera()
        pygame.mouse.set_visible(False)
        menu_condition = False
        game_condition = True

    if game_condition:
        running = True
        game(screen, WIDTH, HEIGHT, clock, FPS, running)
        all_sprites.clear(screen, background)
        game_condition = False
        end_condition = True

    if end_condition:
        new_game = end_screen(screen, WIDTH, HEIGHT, clock, FPS, player.game_result)
        end_condition = False
        if new_game:
            menu_condition = True
        else:
            terminate()