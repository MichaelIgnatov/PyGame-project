from camera import Camera
from start_screen import start_screen
from functions import load_level, generate_level
from variables import *
from main_menu import main_menu
from end_screen import end_screen
import pygame

pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Cube")
clock = pygame.time.Clock()
menu_condition = True
game_condition = False
end_condition = False

background = pygame.image.load('data\image\BackgroundFon.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())


def game(screen, WIDTH, HEIGHT, clock, FPS, running, object_list):
    pygame.mixer.music.load("data/sounds/fon_music.mp3")
    pygame.mixer.music.set_volume(0.4)
    one_iter = True
    while running:
        screen.fill(BLACK)
        clock.tick(FPS)
        player.set_object_list(object_list)

        if one_iter:
            pygame.mixer.music.play(-1)
            one_iter = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                player.update(event.key, object_list)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.update(pygame.K_d, object_list)
        if keys[pygame.K_a]:
            player.update(pygame.K_a, object_list)

        enemies_group.update(player)

        coins_group.update(player)

        portal_group.update()

        screen.blit(background, (0, 0))
        camera.update(player, WIDTH, HEIGHT)
        player.health_display(screen)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        pygame.display.flip()
        if player.death:
            running = False
    pygame.mixer.music.stop()
    screen.fill(BLACK)


def proccess():
    global menu_condition, game_condition, end_condition, player, object_list
    if menu_condition:
        pygame.display.flip()
        level = main_menu(screen, WIDTH, HEIGHT, clock, FPS)
        player, level_x, level_y, object_list = generate_level(load_level(level), object_list)
        player.set_current_level(level)

        pygame.mouse.set_visible(False)


def game_condition():
    global object_list
    running = True
    game(screen, WIDTH, HEIGHT, clock, FPS, running, object_list)
    all_sprites.clear(screen, background)
    object_list = [object_list[i].kill() for i in range(len(object_list))]
    object_list.clear()


def end_condition():
    end_screen(screen, WIDTH, HEIGHT, clock, FPS, player.game_result)


start_screen(screen, WIDTH, HEIGHT, clock, FPS)
main_running = True

object_list = []
player = None
while main_running:
    camera = Camera()
    proccess()
    game_condition()
    end_condition()
