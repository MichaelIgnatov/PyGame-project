import pygame
from variables import *


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
                player.hurt(self.damage, RedBall)
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

    def animation(self):  # Анимация
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
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 0
        self.damage = 1
        self.left_movement = boss_left_movement
        self.right_movement = boss_right_movement
        self.count = 0
        self.direction = ''
        self.set_direction_r = False
        self.set_direction_l = False

    def update(self, player):  # поведение противников
        if self.health == 0:
            self.kill()
        else:
            if abs(self.rect.x - player.rect.x) <= 300:
                self.rect = self.rect.move(self.speed, 0)

                if self.count > 35:
                    self.count = 0
                self.animation()
                self.count += 1

                if player.rect.x < self.rect.x:
                    self.speed = -5
                    self.direction = 'left'

                if player.rect.x > self.rect.x:
                    self.speed = 5
                    self.direction = 'right'

                if pygame.sprite.spritecollideany(self, enemies_border_group):
                    self.speed *= -1
                    if self.direction == 'left':
                        self.direction = 'right'
                    else:
                        self.direction = 'left'

                if pygame.sprite.collide_mask(self, player):
                    if player.player_position != 'top':
                        player.hurt(self.damage)
                    else:
                        self.hurt(player.get_damage())

    def animation(self):  # Анимация
        if self.direction == 'right':
            self.image = self.right_movement[self.count // 5]
        if self.direction == 'left':
            self.image = self.left_movement[self.count // 5]

    def hurt(self, dmg):
        self.health -= dmg


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = bullet_animation[0]
        self.type = 'bullet'
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.damage = 1
        self.count = 0
        self.speed = -10

    def update(self, player):
        if self.count > 5:
            self.count = 0
        self.count += 1
        self.animation()
        self.rect = self.rect.move(self.speed, 0)
        if pygame.sprite.spritecollideany(self, enemies_group) \
                or pygame.sprite.spritecollideany(self, box_group) \
                or pygame.sprite.spritecollideany(self, stone_wall_group) \
                or pygame.sprite.spritecollideany(self, border_group) \
                or pygame.sprite.spritecollideany(self, enemies_border_group)\
                or self.rect.x < 0 or self.rect.x > WIDTH:
            self.kill()
        if pygame.sprite.collide_mask(self, player):
            player.hurt(self.damage, self.type)

    def animation(self):
        self.image = bullet_animation[self.count // 5]


class BlackBall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemies_group, all_sprites)
        self.image = black_ball_image
        self.health = 1
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.damage = 1
        self.count = 0

    def update(self, player=None):
        if self.health <= 0:
            self.kill()
        else:
            if self.count > 35:
                self.count = 0

            if self.count == 35:
                bullets.append(Bullet(self.rect.x, self.rect.y))

            self.count += 1

    def hurt(self, dmg):
        self.health -= dmg
