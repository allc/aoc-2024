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

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            steps = []
            for di, dj in directions:
                i_, j_ = i + di, j + dj
                if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[i_]):
                    if isinstance(grid[i_][j_], int):
                        steps.append(grid[i_][j_])
            if len(steps) < 2:
                continue
            smin = min(steps)
            smax = max(steps)
            saves = smax - smin - 1
            if saves >= 100:
                count += 1
print(count)
