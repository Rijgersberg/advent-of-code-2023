from tqdm import tqdm

from aoc import get_input

def diff(values):
    return [v2 - v1 for v1, v2 in zip(values[:-1], values[1:])]

def allzeroes(values):
    return all(v == 0 for v in values)

# 9-1
total = 0
for values in tqdm(get_input(day=9)):
    values = [int(v) for v in values.split()]

    d = [values]
    while not allzeroes(d[-1]):
        d.append(diff(d[-1]))
    
    d[-1].append(0)
    for i in range(len(d)-2, -1, -1):
        d[i].append(d[i][-1] + d[i+1][-1])
    
    total += d[0][-1]
print(total)

# 9-2
total = 0
for values in tqdm(get_input(day=9)):
    values = [int(v) for v in values.split()]

    d = [values]
    while not allzeroes(d[-1]):
        d.append(diff(d[-1]))
    
    d[-1] = [0] + d[-1]
    for i in range(len(d)-2, -1, -1):
        d[i] = [d[i][0] - d[i+1][0]]
    
    total += d[0][0]
print(total)