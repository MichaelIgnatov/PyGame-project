from camera import Camera
from start_screen import start_screen
from functions import load_level, generate_level
from object_sprites import all_sprites, enemies_group, coins_group, portal_group
from main_menu import main_menu
import pygame

pygame.init()
size = WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Cube")
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
clock = pygame.time.Clock()
FPS = 30

background = pygame.image.load('data\BackgroundFon.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

start_screen(screen, WIDTH, HEIGHT, clock, FPS)
level = main_menu(screen, WIDTH, HEIGHT, clock, FPS)

pygame.mouse.set_visible(False)
player, level_x, level_y = generate_level(load_level(level))
camera = Camera()
running = True

while running:
    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    enemies_group.update(player)

    coins_group.update(player)

    portal_group.update()

    screen.blit(background, (0, 0))
    camera.update(player, WIDTH, HEIGHT)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
