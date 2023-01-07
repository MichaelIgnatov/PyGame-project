import sys
import pygame
from player import Player
from game_objects import Box, StoneWall, Spike, Coin, Portal, Border
from game_enemies import RedBall


# получение файла уровня
def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    return level_map


# Создание игровых объектов
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Box('box', x, y)
            elif level[y][x] == ':':
                StoneWall('stone_wall', x, y)
            elif level[y][x] == 'e':
                RedBall(x, y)
            elif level[y][x] == '^':
                Spike('spike', x, y)
            elif level[y][x] == 'o':
                Portal('portal', x, y)
            elif level[y][x] == '|':
                Border('border', x, y)
            elif level[y][x] == '$':
                Coin('coin', x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)
    return new_player, x, y


# Размещение текста
def place_text(screen, text, x, y, font_size=36):
    font = pygame.font.Font(None, font_size)
    text = font.render(str(text), True, (11, 191, 83))
    screen.blit(text, (x, y))


def terminate():
    pygame.quit()
    sys.exit()
