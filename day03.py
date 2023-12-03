from collections import defaultdict
from functools import cache

from aoc import get_input


@cache
def find_number(line, pos):
    if pos < 0 or pos >= len(line):
        return None
    
    char = line[pos]

    if char.isdigit():
        number = char
    else: 
        return None
    
    # backward
    p_min = pos
    for p in range(pos-1, -1, -1):
        char = line[p]
        if char.isdigit():
            number = char + number
            p_min = p
        else:
            break
    
    # forward
    p_max = pos
    for p in range(pos+1, len(line)):
        char = line[p]
        if char.isdigit():
            number = number + char
            p_max = p
        else:
            break
    
    return int(number), (p_min, p_max)

def parse(lines):
    schematic = defaultdict(str)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            schematic[(r, c)] = char
    return schematic

def neighbors(r, c, R, C):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr, dc) != (0, 0) and 0 <= r+dr < R and 0 <= c+dc < C:
                yield (r+dr, c+dc)

#1
lines = get_input(day=3)
schematic = parse(lines)

numbers = set()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if not char.isdigit() and char != '.':
            for rn, cn in neighbors(r, c, R=len(lines), C=len(line)):
                result = find_number(lines[rn], cn)
                if result is not None:
                    number, (c_min, c_max) = result
                    numbers.add((number, (rn, c_min, c_max)))
print(sum(n for n, pos in numbers))

#2
gear_total = 0
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == '*':
            results = [find_number(lines[rn], cn) 
                       for rn, cn in neighbors(r, c, R=len(lines), C=len(line))]
            results = set(r for r in results if r is not None)
            if len(results) == 2:
                (n1, pos), (n2, pos) = results
                gear_total += n1 * n2
print(gear_total)
