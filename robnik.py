from camera import Camera
from start_screen import start_screen
from functions import load_level, generate_level
from variables import all_sprites, enemies_group, coins_group, portal_group
from main_menu import main_menu
from end_screen import end_screen
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()


pygame.init()
size = WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Cube")
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
clock = pygame.time.Clock()
FPS = 30
new_game = False
one_repetition = True
pygame.mixer.music.load("data/sounds/fon_music.mp3")
pygame.mixer.music.set_volume(0.4)

background = pygame.image.load('data\BackgroundFon.png').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

start_screen(screen, WIDTH, HEIGHT, clock, FPS)
level = main_menu(screen, WIDTH, HEIGHT, clock, FPS)

pygame.mouse.set_visible(False)
player, level_x, level_y = generate_level(load_level(level))
player.set_current_level(level)
camera = Camera()
running = True

while running:
    if one_repetition:
        pygame.mixer.music.play(-1)
        one_repetition = False

    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player.update(event.key)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.update(pygame.K_w)
    if keys[pygame.K_s]:
        player.update(pygame.K_s)
    if keys[pygame.K_d]:
        player.update(pygame.K_d)
    if keys[pygame.K_a]:
        player.update(pygame.K_a)

    player.health_display(screen)

    enemies_group.update(player)

    coins_group.update(player)

    portal_group.update()

    screen.blit(background, (0, 0))
    camera.update(player, WIDTH, HEIGHT)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()

    if player.get_game_result() != '':
        pygame.mixer.music.stop()
        game_result = player.get_game_result()
        end_screen(screen, WIDTH, HEIGHT, clock, FPS, game_result)
        running = False
pygame.quit()















if args[0] == pygame.K_w:
    self.rect = self.rect.move(0, -1 * self.speed)
    if pygame.sprite.spritecollideany(self, box_group) \
            or pygame.sprite.spritecollideany(self, stone_wall_group) \
            or pygame.sprite.spritecollideany(self, border_group) \
            or pygame.sprite.spritecollideany(self, enemies_border_group):
        self.rect = self.rect.move(0, self.speed)
    if pygame.sprite.spritecollideany(self, portal_group):
        self.sound_portal.play()
        self.rect = self.rect.move(0, self.speed)
        self.kill()
        self.game_result = 'win'
        self.death = True
if args[0] == pygame.K_s:
    self.rect = self.rect.move(0, self.speed)
    if pygame.sprite.spritecollideany(self, box_group) \
            or pygame.sprite.spritecollideany(self, stone_wall_group) \
            or pygame.sprite.spritecollideany(self, border_group) \
            or pygame.sprite.spritecollideany(self, enemies_border_group):
        self.rect = self.rect.move(0, -1 * self.speed)
    if pygame.sprite.spritecollideany(self, portal_group):
        self.sound_portal.play()
        self.rect = self.rect.move(0, -1 * self.speed)
        self.kill()
        self.game_result = 'win'
        self.death = True
    if pygame.sprite.spritecollideany(self, enemies_group):
        self.player_position = 'top'

    import pygame
    from variables import player_group, all_sprites, box_group, player_image, tile_width, tile_height, \
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
            self.yvel = 0
            self.onGround = False
            self.JUMP_POWER = 10
            self.GRAVITY = 0.35

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
                        self.rect = self.rect.move(-1 * self.speed, 0)
                        if pygame.sprite.spritecollideany(self, box_group) \
                                or pygame.sprite.spritecollideany(self, stone_wall_group) \
                                or pygame.sprite.spritecollideany(self, border_group) \
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

        def collide(self):
            if not self.onGround:
                self.rect = self.rect.move(0, 10)
            if pygame.sprite.spritecollideany(self, box_group) \
                    or pygame.sprite.spritecollideany(self, stone_wall_group) \
                    or pygame.sprite.spritecollideany(self, border_group) \
                    or pygame.sprite.spritecollideany(self, enemies_border_group):
                self.onGround = True
                self.rect = self.rect.move(0, -10)

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


