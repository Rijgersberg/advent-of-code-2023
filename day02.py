import re

from aoc import get_input

maximum = {
    'red': 12,
    'green': 13,
    'blue': 14
}
def parse(game):
    for draw in game.strip().split(';'):
        for color in draw.strip().split(','):
            number, colorname = color.strip().split()
            yield int(number), colorname

def possible(game):
    for number, colorname in parse(game):
        if number > maximum[colorname]:
            return False
    return True

def power(game):
    minimum = {'red': 0, 'green': 0, 'blue': 0}
    for number, colorname in parse(game):
        minimum[colorname] = max(number, minimum[colorname])
    return minimum['red'] * minimum['green'] * minimum['blue']


total_ids = 0
total_power = 0
for line in get_input(day=2):
    id_part, game = line.split(':')
    id = int(id_part.split()[1])
    
    if possible(game.strip()):
        total_ids += id
    total_power += power(game.strip())
print(total_ids)
print(total_power)