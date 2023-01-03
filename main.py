from Camera import Camera
from Start_screen import start_screen
from Level import load_level, generate_level
from Sprites import all_sprites, enemies_group
import pygame

pygame.init()
size = WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Cube")
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
clock = pygame.time.Clock()
FPS = 30
pygame.mouse.set_visible(False)

background = pygame.image.load('data\BackgroundFon.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

start_screen(screen, WIDTH, HEIGHT, clock, FPS)
player, level_x, level_y, enemies_list = generate_level(load_level('test_level.txt'))
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

    for enemie in enemies_list:
        enemie.update()  # обновление положения противников

    screen.blit(background, (0, 0))
    camera.update(player, WIDTH, HEIGHT)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
