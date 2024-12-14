robots = []

input_file = 'input.txt'
width = 101
height = 103
seconds = 100

with open(input_file) as f:
    for line in f:
        p, v = tuple(a[2:] for a in line.strip().split())
        p = tuple(map(int, p.split(',')))
        v = tuple(map(int, v.split(',')))
        robots.append((p, v))

new_positions = []
for r in robots:
    new_col = (r[0][0] + r[1][0] * seconds) % width
    new_row = (r[0][1] + r[1][1] * seconds) % height
    new_positions.append((new_col, new_row))

q_width = width // 2
q_height = height // 2

counts = [0] * 4

for p in new_positions:
    if p[0] > q_width and p[1] < q_height:
        counts[0] += 1
    elif p[0] < q_width and p[1] < q_height:
        counts[1] += 1
    elif p[0] < q_width and p[1] > q_height:
        counts[2] += 1
    elif p[0] > q_width and p[1] > q_height:
        counts[3] += 1

import math

print(math.prod(counts))
