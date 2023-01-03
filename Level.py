from Player import Player
from Game_objects import Box, StoneWall, Spike
from Game_enemies import RedBall

# получение файла уровня
def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # max_width = max(map(len, level_map))

    return level_map

# Создание игровых объектов
def generate_level(level):
    enemies_list = []
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Box('box', x, y)
            elif level[y][x] == ':':
                StoneWall('stone_wall', x, y)
            elif level[y][x] == 'e':
                enemie = RedBall(x, y)
                enemies_list.append(enemie)  # список всех противников
            elif level[y][x] == '^':
                Spike('spike', x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)
    return new_player, x, y, enemies_list