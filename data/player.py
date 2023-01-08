import pygame
from object_sprites import player_group, all_sprites, box_group, player_image, tile_width, tile_height, \
    stone_wall_group, portal_group, border_group, enemies_border_group
from load_image import load_image


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
        self.sound_coin = pygame.mixer.Sound("data/sounds/take a coin.ogg")
        self.sound_hurt = pygame.mixer.Sound("data/sounds/player_hurt.ogg")
        self.sound_portal = pygame.mixer.Sound("data/sounds/portal.ogg")
        self.full_heart = load_image('heart.png')
        self.empty_heart = load_image('empty_heart.png')
        self.heart_list = [self.full_heart, self.full_heart, self.full_heart]
        self.heart_x = 50
        self.heart_y = 50

    def update(self, *args):
        if self.health <= 0:
            self.death = True
            self.game_result = 'lose'
            self.kill()
        else:  # обработка столкновений с игровыми объектами
            if args:
                if args[0] == pygame.K_SPACE:
                    pass
                if args[0] == pygame.K_d:
                    self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group)\
                            or pygame.sprite.spritecollideany(self, enemies_border_group):
                        self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.sound_portal.play()
                        self.rect = self.rect.move(-1 * self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
                if args[0] == pygame.K_a:
                    self.rect = self.rect.move(-1 * self.speed, 0)
                    if pygame.sprite.spritecollideany(self, box_group) \
                            or pygame.sprite.spritecollideany(self, stone_wall_group) \
                            or pygame.sprite.spritecollideany(self, border_group)\
                            or pygame.sprite.spritecollideany(self, enemies_border_group):
                        self.rect = self.rect.move(self.speed, 0)
                    if pygame.sprite.spritecollideany(self, portal_group):
                        self.sound_portal.play()
                        self.rect = self.rect.move(self.speed, 0)
                        self.kill()
                        self.game_result = 'win'
                        self.death = True
        if self.death:
            self.save_result()

    def hurt(self, dmg):  # Нанесение повреждений игроку
        self.sound_hurt.play()
        self.health -= dmg

    def take_coin(self):  # Подсчёт собранных игроком монет
        self.sound_coin.play()
        self.coins += 1

    def set_current_level(self, level):  # Устанавливает текущий уровень
        self.current_level = level

    def get_game_result(self):  # Возвращает результат текущей игры
        return self.game_result

    def get_position(self):
        return self.player_position

    def get_damage(self):
        return self.damage

    def health_display(self, screen):
        for heart in self.heart_list:
            screen.blit(heart, (self.heart_x, self.heart_y))
            self.heart_x += 60

    def save_result(self):  # Сохранение результата игры в текстовый файл
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

    def erase(self):
        self.kill()
