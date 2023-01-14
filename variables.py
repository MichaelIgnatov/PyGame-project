import pygame
from load_image import load_image
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


BLACK = pygame.Color('black')
WIDTH, HEIGHT = 700, 600
FPS = 30
START_SOUND = pygame.mixer.Sound("data/sounds/start_sound.ogg")
LOSE_SOUND = pygame.mixer.Sound("data/sounds/game-lose.ogg")
WIN_SOUND = pygame.mixer.Sound("data/sounds/game-win.ogg")

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
enemies_border_group = pygame.sprite.Group()

tile_images = {
    'box': load_image('box.png'),
    'stone_wall': load_image('stone wall.png'),
    'spike': load_image('spike.png'),
    'coin': load_image('coin.png'),
    'portal': load_image('portal1.png'),
    'border': load_image('border.png'),
    'enemies_border': load_image('box.png')
}
#  Список спрайтов для анимации перемещения RedBall влево
left_movement = [load_image('RedBall_left_45_rotate.png'), load_image('RedBall_left_90_rotate.png'),
                 load_image('RedBall_left_135_rotate.png'), load_image('RedBall_180_rotate.png'),
                 load_image('RedBall_right_135_rotate.png'), load_image('RedBall_right_90_rotate.png'),
                 load_image('RedBall_right_45_rotate.png'), load_image('RedBall.png')]

#  Список спрайтов для анимации перемещения RedBall вправо
right_movement = [load_image('RedBall_right_45_rotate.png'), load_image('RedBall_right_90_rotate.png'),
                  load_image('RedBall_right_135_rotate.png'), load_image('RedBall_180_rotate.png'),
                  load_image('RedBall_left_135_rotate.png'), load_image('RedBall_left_90_rotate.png'),
                  load_image('RedBall_left_45_rotate.png'), load_image('RedBall.png')]

#  Список спрайтов для анимации монетки
coins_animation = [load_image('coin.png'), load_image('coin1.png'),
                   load_image('coin2.png'), load_image('coin3.png'),
                   load_image('coin4.png'), load_image('coin4.png')]

#  Список спрайтов для анимации порталов
portal_animation = [load_image('portal1.png'), load_image('portal2.png'), load_image('portal3.png'),
                    load_image('portal4.png')]

#  Список спрайтов для анимации перемещения Boss влево
boss_left_movement = [load_image('Boss_left_45_rotate.png'), load_image('Boss_left_90_rotate.png'),
                 load_image('Boss_left_135_rotate.png'), load_image('Boss_180_rotate.png'),
                 load_image('Boss_right_135_rotate.png'), load_image('Boss_right_90_rotate.png'),
                 load_image('Boss_right_45_rotate.png'), load_image('Boss.png')]

#  Список спрайтов для анимации перемещения Boss вправо
boss_right_movement = [load_image('Boss_right_45_rotate.png'), load_image('Boss_right_90_rotate.png'),
                  load_image('Boss_right_135_rotate.png'), load_image('Boss_180_rotate.png'),
                  load_image('Boss_left_135_rotate.png'), load_image('Boss_left_90_rotate.png'),
                  load_image('Boss_left_45_rotate.png'), load_image('Boss.png')]

player_image = load_image('player.png')  # Спрайт игрока
red_ball_image = load_image('RedBall.png')  # Спрайт RedBall
boss_image = load_image('Boss.png')  # Спрайт Boss

delighted_player_image = load_image('delighted_player.jpg')
sad_player_image = load_image('sad_player.jpg')

tile_width = tile_height = 50
