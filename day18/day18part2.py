grid_size = 71
n_bytes = 1024
input_file = 'input.txt'

falling_bytes = []
with open(input_file) as f:
    falling_bytes = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]
print(falling_bytes)

grid = [['.'] * grid_size for _ in range(grid_size)]

def print_grid(grid):
    for row in grid:
        print(''.join(row))

for b in falling_bytes[:n_bytes]:
    grid[b[0]][b[1]] = '#'

print_grid(grid)

start = (0, 0)
end = (grid_size - 1, grid_size - 1)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for b in falling_bytes[n_bytes:]:
    is_solution_found = False
    grid[b[0]][b[1]] = '#'
    # bfs
    visited = [[False] * grid_size for _ in range(grid_size)]
    to_search = [(start, 0)]
    while to_search:
        (i, j), d = to_search.pop(0)
        if (i, j) == end:
            is_solution_found = True
            break
        for (di, dj) in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < grid_size and 0 <= nj < grid_size:
                if not visited[ni][nj] and grid[ni][nj] != '#':
                    to_search.append(((ni, nj), d + 1))
                    visited[ni][nj] = True
    if not is_solution_found:
        print(b)
        break
