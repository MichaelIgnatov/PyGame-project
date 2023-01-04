import pygame
from load_image import load_image

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
stone_wall_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()

tile_images = {
    'box': load_image('box.png'),
    'stone_wall': load_image('stone wall.png'),
    'spike': load_image('spike.png')
}

left_movement = [load_image('RedBall_left_90_rotate.png'), load_image('RedBall_180_rotate.png'),
                 load_image('RedBall_right_90_rotate.png'), load_image('RedBall.png')]

right_movement = [load_image('RedBall_right_90_rotate.png'), load_image('RedBall_180_rotate.png'),
                 load_image('RedBall_left_90_rotate.png'), load_image('RedBall.png')]

player_image = load_image('player.png')
red_ball_image = load_image('RedBall.png')
boss_image = load_image('Boss.png')

tile_width = tile_height = 50
