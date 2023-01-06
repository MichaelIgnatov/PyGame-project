import pygame
from object_sprites import player_group, all_sprites, box_group, player_image, tile_width, tile_height, \
    stone_wall_group, portal_group, border_group


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
        self.death = False
        self.current_level = ''
        self.game_result = ''

    def update(self, *args):
        if self.health <= 0:
            self.death = True
            self.game_result = 'lose'
            self.kill()
        else:  # обработка столкновений с игровыми объектами
            if args:
                if args[0] == pygame.K_w:
                    self.rect = self.rect.move(0, -1 * self.speed)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group):
                        self.rect = self.rect.move(0, self.speed)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.rect = self.rect.move(0, self.speed)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
                if args[0] == pygame.K_s:
                    self.rect = self.rect.move(0, self.speed)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group):
                        self.rect = self.rect.move(0, -1 * self.speed)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.rect = self.rect.move(0, -1 * self.speed)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
                if args[0] == pygame.K_d:
                    self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
                if args[0] == pygame.K_a:
                    self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group):
                        self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.rect = self.rect.move(self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
        if self.death:
            self.save_result()

    def hurt(self, dmg):
        self.health -= dmg

    def take_coin(self):
        self.coins += 1

    def set_current_level(self, level):
        self.current_level = level

    def get_game_result(self):
        return self.game_result

    def save_result(self):
        file = open("data/result.txt", "r", encoding='utf8')
        text = file.read().strip().split()
        file.close()

        current_result = self.coins
        text[3] = str(current_result)

        if self.current_level == 'level1.txt' and int(text[0]) < current_result:
            text[0] = str(current_result)
        if self.current_level == 'level2.txt' and int(text[1]) < current_result:
            text[1] = str(current_result)
        if self.current_level == 'level3.txt' and int(text[2]) < current_result:
            text[2] = str(current_result)

        file = open("data/result.txt", "w", encoding='utf8')
        file.write(' '.join(text))
        file.close()
