import sys
import pygame
from player import Player
from game_objects import Box, StoneWall, Spike, Coin, Portal, Border, EnemiesBorder
from game_enemies import RedBall, Boss


# получение файла уровня
def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    return level_map


# Создание игровых объектов
def generate_level(level, ls):
    object_list = ls
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                object_list.append(Box('box', x, y))
            elif level[y][x] == ':':
                object_list.append(StoneWall('stone_wall', x, y))
            elif level[y][x] == 'e':
                object_list.append(RedBall(x, y))
            elif level[y][x] == 'B':
                object_list.append(Boss(x, y))
            elif level[y][x] == '^':
                object_list.append(Spike('spike', x, y))
            elif level[y][x] == 'o':
                object_list.append(Portal('portal', x, y))
            elif level[y][x] == '|':
                object_list.append(Border('border', x, y))
            elif level[y][x] == '$':
                object_list.append(Coin('coin', x, y))
            elif level[y][x] == 'b':
                object_list.append(EnemiesBorder('enemies_border', x, y))
            elif level[y][x] == '@':
                new_player = Player(x, y)
    return new_player, x, y, object_list


# Размещение текста
def place_text(screen, text, x, y, font_size=36):
    font = pygame.font.Font(None, font_size)
    text = font.render(str(text), True, (11, 191, 83))
    screen.blit(text, (x, y))


def terminate():
    pygame.quit()
    sys.exit()
