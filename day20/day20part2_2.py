with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]
for i, row in enumerate(grid):
    print(f'{i:02}', ''.join(row))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'E':
            end = (i, j)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_shortest_paths(grid):
    partial_paths = [[start]]
    while partial_paths:
        path = partial_paths.pop()
        i, j = path[-1]
        if path[-1] == end:
            return path
        for di, dj in directions:
            i_, j_ = i + di, j + dj
            if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[i_]):
                if (i_, j_) in path:
                    continue
                if grid[i_][j_] == '#':
                    continue
                partial_paths.append(path + [(i_, j_)])

path = find_shortest_paths(grid)
# Time taken is path length - 1
# There is only one path
for s, p in enumerate(path):
    i, j = p
    grid[i][j] = s

n_cheats_time = 20
count = 0
for a, (i1, j1) in enumerate(path):
    for b, (i2, j2) in enumerate(path[a + 1:]):
        if abs(i1 - i2) + abs(j1 - j2) > n_cheats_time:
            continue
        saves = b + 1 - (abs(i1 - i2) + abs(j1 - j2))
        if saves >= 100:
            count += 1
print(count)
