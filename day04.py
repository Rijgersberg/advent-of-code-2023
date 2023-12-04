import re
from collections import deque

from aoc import get_input


def parse(lines):
    pattern = r'Card +(\d+): ([\d ]+) \| ([\d ]+)'
    for line in lines:
        matches = re.match(pattern, line)
        card, winning, chosen = matches.groups()
        card = int(card)
        winning = {int(n) for n in winning.strip().split()}
        chosen = {int(n) for n in chosen.strip().split()}

        yield card, winning, chosen

# 1
total_score = 0
for card, winning, chosen in parse(get_input(day=4)):
    n = len(chosen & winning)
    score = 2**(n-1) if n > 0 else 0
    total_score += score
print(total_score)

#2
cards = {n: (winning, chosen) for n, winning, chosen in parse(get_input(day=4))}

queue = deque()
queue.extend((1, c) for c in cards.keys())

total = 0
while queue:
    n, c = queue.popleft()
    total += n

    winning, chosen = cards[c]
    for new in range(c+1, c+1+len(winning & chosen)):
        queue.append((n, new))
print(total)
