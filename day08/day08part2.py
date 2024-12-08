grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))

from collections import defaultdict
antennas = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.' and grid[i][j] != '#':
            antennas[grid[i][j]].append((i, j))

print(antennas)

antinodes = set()

import math

for _, A in antennas.items():
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            x1, y1 = A[i]
            x2, y2 = A[j]
            dx = x1 - x2
            dy = y1 - y2
            print(dx, dy)
            d = math.gcd(abs(dx), abs(dy))
            dx //= d
            dy //= d
            x1_, y1_ = x1, y1
            while x1_ >= 0 and x1_ < len(grid) and y1_ >= 0 and y1_ < len(grid[0]):
                antinodes.add((x1_, y1_))
                x1_ += dx
                y1_ += dy
            x1_, y1_ = x1, y1
            while x1_ >= 0 and x1_ < len(grid) and y1_ >= 0 and y1_ < len(grid[0]):
                antinodes.add((x1_, y1_))
                x1_ -= dx
                y1_ -= dy

print(antinodes)
print(len(antinodes))