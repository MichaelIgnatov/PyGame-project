import pygame
from object_sprites import player_group, all_sprites, box_group, player_image, tile_width, tile_height, \
    stone_wall_group, spike_group, enemies_group


# класс игрового персонажа

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.health = 3
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.speed = 10
        self.damage = 1
        self.coins = 0

    def update(self, *args):
        if self.health <= 0:
            self.kill()
        else:  # обработка столкновений с игровыми объектами
            if args:
                if args[0] == pygame.K_w:
                    self.rect = self.rect.move(0, -1 * self.speed)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group):
                        self.rect = self.rect.move(0, self.speed)
                if args[0] == pygame.K_s:
                    self.rect = self.rect.move(0, self.speed)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group):
                        self.rect = self.rect.move(0, -1 * self.speed)
                if args[0] == pygame.K_d:
                    self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                if args[0] == pygame.K_a:
                    self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group):
                        self.rect = self.rect.move(self.speed, 0)

    def hurt(self, dmg):
        self.health -= dmg

    def take_coin(self):
        self.coins += 1
