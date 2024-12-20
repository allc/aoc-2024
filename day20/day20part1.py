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

shortest_without_cheats = float('inf')

for n_cheats_time in range(0, 2):
    paths = []
    partial_paths = [([start], [])]
    while partial_paths:
        path, cheats = partial_paths.pop()
        i, j = path[-1]
        if path[-1] == end:
            paths.append((path, cheats.copy()))
            print(len(paths))
            continue
        for di, dj in directions:
            i_, j_ = i + di, j + dj
            if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[i_]):
                if (i_, j_) in path:
                    continue
                if grid[i_][j_] == '#':
                    if n_cheats_time > len(cheats):
                        partial_paths.append((path + [(i_, j_)], cheats + [(i_, j_)]))
                else:
                    cheat_ = cheats + [(i_, j_)] if 0 < len(cheats) < n_cheats_time else cheats.copy()
                    partial_paths.append((path + [(i_, j_)], cheat_))
    paths.sort(key=lambda x: len(x[0]))
    if n_cheats_time == 0:
        shortest_without_cheats = len(paths[0][0]) - 1
    else:
        paths = [(path, cheats) for path, cheats in paths if len(path) - 1 < shortest_without_cheats]
    print(len(paths), [len(path) - 1 for path, _ in paths])
    print([cheats for _, cheats in paths])

    #TODO: cheak cheats are unique
