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

for _, A in antennas.items():
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            x1, y1 = A[i]
            x2, y2 = A[j]
            x = x1 - (x2 - x1)
            y = y1 - (y2 - y1)
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                antinodes.add((x, y))
            x = x2 + (x2 - x1)
            y = y2 + (y2 - y1)
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                antinodes.add((x, y))

print(antinodes)
print(len(antinodes))