import pygame
from load_image import load_image

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
stone_wall_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
border_group = pygame.sprite.Group()

tile_images = {
    'box': load_image('box.png'),
    'stone_wall': load_image('stone wall.png'),
    'spike': load_image('spike.png'),
    'coin': load_image('coin.png'),
    'portal': load_image('portal1.png'),
    'border': load_image('border.png')
}

left_movement = [load_image('RedBall_left_45_rotate.png'), load_image('RedBall_left_90_rotate.png'),
                 load_image('RedBall_left_135_rotate.png'), load_image('RedBall_180_rotate.png'),
                 load_image('RedBall_right_135_rotate.png'), load_image('RedBall_right_90_rotate.png'),
                 load_image('RedBall_right_45_rotate.png'), load_image('RedBall.png')]

right_movement = [load_image('RedBall_right_45_rotate.png'), load_image('RedBall_right_90_rotate.png'),
                  load_image('RedBall_right_135_rotate.png'), load_image('RedBall_180_rotate.png'),
                  load_image('RedBall_left_135_rotate.png'), load_image('RedBall_left_90_rotate.png'),
                  load_image('RedBall_left_45_rotate.png'), load_image('RedBall.png')]

coins_animation = [load_image('coin.png'), load_image('coin1.png'),
                   load_image('coin2.png'), load_image('coin3.png'),
                   load_image('coin4.png'), load_image('coin4.png')]

portal_animation = [load_image('portal1.png'), load_image('portal2.png'), load_image('portal3.png'),
                    load_image('portal4.png')]

player_image = load_image('player.png')
red_ball_image = load_image('RedBall.png')
boss_image = load_image('Boss.png')

tile_width = tile_height = 50
