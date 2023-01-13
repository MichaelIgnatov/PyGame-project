import pygame
from object_sprites import enemies_group, all_sprites, red_ball_image, tile_width, tile_height, boss_image, \
    left_movement, right_movement, enemies_border_group, boss_left_movement, boss_right_movement


# классы противников


class RedBall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemies_group, all_sprites)
        self.image = red_ball_image
        self.left_movement = left_movement
        self.right_movement = right_movement
        self.count = 0
        self.direction = 'right'
        self.health = 1
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 2
        self.damage = 1

    def update(self, player):  # поведение противников
        if self.health == 0:
            self.kill()
        self.rect = self.rect.move(self.speed, 0)
        if pygame.sprite.collide_mask(self, player):
            if player.player_position != 'top':
                player.hurt(self.damage)
            else:
                self.hurt(player.get_damage())

        if self.count > 35:
            self.count = 0
        self.animation()
        self.count += 1
        if pygame.sprite.spritecollideany(self, enemies_border_group):
            self.speed *= -1
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'

        self.animation()

    def animation(self):
        if self.direction == 'right':
            self.image = self.right_movement[self.count // 5]
        if self.direction == 'left':
            self.image = self.left_movement[self.count // 5]

    def hurt(self, dmg):
        self.health -= dmg


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemies_group, all_sprites)
        self.image = boss_image
        self.health = 5
        self.rect = self.image. \
            get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 5
        self.damage = 1
        self.left_movement = boss_left_movement
        self.right_movement = boss_right_movement
        self.count = 0
        self.direction = ''

    def update(self, player):  # поведение противников
        if self.health == 0:
            self.kill()
        else:
            if abs(self.rect.x - player.rect.x) <= 40:
                if self.rect.x - player.rect.x <= 0:
                    self.direction = 'left'
                    self.speed *= -1
                else:
                    self.direction = 'right'
                if self.health == 0:
                    self.kill()
                self.rect = self.rect.move(self.speed, 0)
                if pygame.sprite.spritecollideany(self, enemies_border_group):
                    self.speed *= -1
                if pygame.sprite.collide_mask(self, player):
                    if player.player_position != 'top':
                        player.hurt(self.damage)
                    else:
                        self.hurt(player.get_damage())

                if self.count > 35:
                    self.count = 0
                self.animation()
                self.count += 1
            self.rect = self.rect.move(self.speed, 0)

    def animation(self):
        if self.direction == 'right':
            self.image = self.right_movement[self.count // 5]
        if self.direction == 'left':
            self.image = self.left_movement[self.count // 5]

    def hurt(self, dmg):
        self.health -= dmg