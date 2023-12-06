import re
from dataclasses import dataclass
from aoc import get_input

@dataclass
class Range:
    source_start: int
    dest_start: int
    range: int

    def check(self, source):
        if source in range(self.source_start, self.source_start + self.range):
            return self.dest_start + (source - self.source_start)


def parse(almanac):
    parts = almanac.split('\n\n')

    seeds = [int(seed) for seed in parts[0].split(':')[1].split()]
    print(seeds)
    
    maps = {}

    pattern = r'(\w+)-to-(\w+) map:'
    for part in parts[1:]:
        lines = part.splitlines()

        source, dest = re.fullmatch(pattern, lines[0]).groups()
        map = []
        for line in lines[1:]:
            dest_n, source_n, r = [int(x) for x in line.split()]
            map.append(Range(source_start=source_n, dest_start=dest_n, range=r))
        maps[(source, dest)] = map
    return seeds, maps

def find_location(seed, maps):
    source = seed
    for key, map in maps.items():
        for range in map:
            if (dest := range.check(source)) is not None:
                source = dest
                break
    return source

        


almanac = get_input(day=5, as_list=False)


seeds, maps = parse(almanac)
min_loc = float('inf')
for seed in seeds:
    min_loc = min(min_loc, find_location(seed, maps))
print(min_loc)
