import pygame
from object_sprites import box_group, all_sprites, tile_images, tile_width, tile_height, stone_wall_group, spike_group, \
    enemies_group


# игровые объекты

# Ящик
class Box(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(box_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# Каменная стена
class StoneWall(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(stone_wall_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# Колючка
class Spike(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(spike_group, enemies_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.damage = 1

    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            player.hurt(self.damage)
