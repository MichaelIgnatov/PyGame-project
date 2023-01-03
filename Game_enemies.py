import pygame
from Sprites import enemies_group, all_sprites, red_ball_image, tile_width, tile_height, box_group, stone_wall_group, \
    spike_group

# классы противников


class RedBall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemies_group, all_sprites)
        self.image = red_ball_image
        self.health = 1
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 15
        self.damage = 1

    def update(self):  # поведение противников
        self.rect = self.rect.move(self.speed, 0)
        if pygame.sprite.spritecollideany(self, box_group) or pygame.sprite.spritecollideany(self, stone_wall_group) \
                or pygame.sprite.spritecollideany(self, spike_group):
            self.rect = self.rect.move(-1 * self.speed, 0)
            self.speed *= -1


class Boss(pygame.sprite.Sprite):
    pass