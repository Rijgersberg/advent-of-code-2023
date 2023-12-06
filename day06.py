from functools import reduce
from operator import mul

from tqdm import tqdm

from aoc import get_input

def parse1(lines):
    times = [int(x) for x in lines[0].split(':')[1].split()]
    distances = [int(x) for x in lines[1].split(':')[1].split()]

    return zip(times, distances, strict=True)

#1
ways = []
for T, D in parse1(get_input(day=6)):
    count = 0
    for t in range(0, T+1):
        d = (T-t) * t
        if d > D:
            count += 1
    ways.append(count)

print(reduce(mul, ways))

#2
def parse2(lines):
    T = int(lines[0].split(':')[1].replace(' ', ''))
    D = int(lines[1].split(':')[1].replace(' ', ''))
    return T, D

T, D = parse2(get_input(day=6))
count = 0
for t in tqdm(range(0, T+1)):
    d = (T-t) * t
    if d > D:
        count += 1
print(count)