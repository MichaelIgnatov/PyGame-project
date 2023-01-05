import pygame
from object_sprites import box_group, all_sprites, tile_images, tile_width, tile_height, stone_wall_group, spike_group, \
    enemies_group, coins_group, coins_animation, portal_group, portal_animation, border_group


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


class Coin(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(coins_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.coins_animation = coins_animation
        self.count = 0

    def update(self, player):
        self.animation()
        self.count += 1
        if pygame.sprite.collide_mask(self, player):
            player.take_coin()
            self.kill()

    def animation(self):
        self.image = self.coins_animation[self.count % 5]


class Portal(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(portal_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.portal_animation = portal_animation
        self.count = 0

    def update(self):
        self.animation()
        self.count += 1

    def animation(self):
        self.image = self.portal_animation[self.count % 4]


class Border(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(border_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
