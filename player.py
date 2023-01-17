import pygame
from variables import *
from load_image import load_image
from game_objects import Box, StoneWall, Border, EnemiesBorder, Spike


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
        self.player_position = ''
        self.current_level = ''
        self.game_result = ''
        self.sound_coin = COIN_SOUND
        self.sound_hurt = SOUND_HURT
        self.sound_portal = SOUND_PORTAL
        self.full_heart = load_image('heart.png')
        self.empty_heart = load_image('empty_heart.png')
        self.heart_list = [self.full_heart, self.full_heart, self.full_heart]
        self.heart_x = 30
        self.heart_y = 30
        self.JUMP_COUNT = 15
        self.jump = 15
        self.is_jump = False
        self.object_list = ''

    def update(self, *args):
        if self.health <= 0:
            self.death = True
            self.game_result = 'lose'
            self.kill()
        else:  # Обработка движения игрока и столкновения с игровыми объектами
            if args:
                if args[0] == pygame.K_SPACE and not self.is_jump:
                    self.is_jump = True
                    self.player_position = 'top'

                if args[0] == pygame.K_d:
                    self.speed = 10
                    self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group) \
                            or pygame.sprite.spritecollideany(self, enemies_border_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.sound_portal.play()
                        self.rect = self.rect.move(-1 * self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True

                if args[0] == pygame.K_a:
                    self.speed = -10
                    self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group) \
                            or pygame.sprite.spritecollideany(self, enemies_border_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.sound_portal.play()
                        self.rect = self.rect.move(-1 * self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
                collide_count = 0

                for elem in self.object_list:
                    if pygame.sprite.collide_rect(self, elem) and type(elem) in [Box, StoneWall, Border, EnemiesBorder]:
                        self.rect.bottom = elem.rect.top
                    if self.rect.bottom == elem.rect.top and abs(self.rect.x - elem.rect.x) < 50 and type(elem) != Spike:
                        collide_count += 1
                        self.player_position = ''

                if collide_count == 0 and not self.is_jump:  # Падение
                    self.rect = self.rect.move(0, 15)
                    self.player_position = 'top'
                    for elem in self.object_list:
                        if pygame.sprite.collide_rect(self, elem) \
                                and type(elem) in [Box, StoneWall, Border, EnemiesBorder]:
                            self.rect.bottom = elem.rect.top
        if self.death:
            self.save_result()

    def hurt(self, dmg, object_type=None):  # Нанесение повреждений игроку
        self.sound_hurt.play()
        self.health -= dmg
        if self.health == 2:
            self.image = delighted_player_image
            self.heart_list[self.health] = self.empty_heart
        if self.health == 1:
            self.image = sad_player_image
            self.heart_list[self.health] = self.empty_heart
        if object_type != None:
            self.discarding(object_type)

    def take_coin(self):  # Подсчёт собранных игроком монет
        self.sound_coin.play()
        self.coins += 1

    def jump(self):  # прыжок
        if self.is_jump:
            if self.JUMP_COUNT >= -1 * self.jump:
                self.rect = self.rect.move(0, -1 * self.jump)
                self.jump -= 1
                for elem in self.object_list:
                    if pygame.sprite.collide_rect(self, elem) \
                            and type(elem) in [Box, StoneWall, Border, EnemiesBorder]:
                        self.rect = self.rect.move(0, self.jump)
                        self.jump = 15
                        self.is_jump = False
                        self.player_position = ''

            else:
                self.jump = 15
                self.is_jump = False
                self.player_position = ''

    def set_object_list(self, object_list):  # Получение списка объектов
        self.object_list = object_list

    def set_current_level(self, level):  # Устанавливает текущий уровень
        self.current_level = level

    def get_game_result(self):  # Возвращает результат текущей игры
        return self.game_result

    def get_position(self):  # Возвращает позицию игрока относительно противника
        return self.player_position

    def get_damage(self):  # Возвращает урон игрока
        return self.damage

    def discarding(self, object_type):  # Что-то напоминающее отбрасывание
        if object_type == 'boss'
            repel = 8
        else:
            repel = 4
        if self.speed < 0:
            self.rect = self.rect.move(self.speed * repel, 0)
            if pygame.sprite.spritecollideany(self, box_group) \
                    or pygame.sprite.spritecollideany(self, stone_wall_group) \
                    or pygame.sprite.spritecollideany(self, border_group) \
                    or pygame.sprite.spritecollideany(self, enemies_border_group):
                self.rect = self.rect.move(self.speed * -repel, 0)
        if self.speed > 0:
            self.rect = self.rect.move(self.speed * -repel, 0)
            if pygame.sprite.spritecollideany(self, box_group) \
                    or pygame.sprite.spritecollideany(self, stone_wall_group) \
                    or pygame.sprite.spritecollideany(self, border_group) \
                    or pygame.sprite.spritecollideany(self, enemies_border_group):
                self.rect = self.rect.move(self.speed * repel, 0)

    def health_display(self, screen):  # Отображение здоровья героя
        self.heart_x = 30
        for heart in self.heart_list:
            screen.blit(heart, (self.heart_x, self.heart_y))
            self.heart_x += 60

    def save_result(self):  # Сохранение результата игры в текстовый файл
        file = open("data/result.txt", "r", encoding='utf8')
        text = file.read().strip().split()
        file.close()

        current_result = self.coins
        text[3] = str(current_result)

        if self.current_level == 'level1.txt' and int(text[0]) < current_result \
                and self.game_result == 'win':
            text[0] = str(current_result)
        if self.current_level == 'level2.txt' and int(text[1]) < current_result \
                and self.game_result == 'win':
            text[1] = str(current_result)
        if self.current_level == 'level3.txt' and int(text[2]) < current_result \
                and self.game_result == 'win':
            text[2] = str(current_result)

        file = open("data/result.txt", "w", encoding='utf8')
        file.write(' '.join(text))
        file.close()

    def erase(self):
        self.kill()
