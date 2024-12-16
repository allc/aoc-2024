grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
for row in grid:
    print(''.join(row))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
print(f'{start = }')
current_direction_i = 0

visited = []
for i in range(len(grid)):
    visited_row = []
    for j in range(len(grid[i])):
        visited_row.append([float('inf')] * 4)
    visited.append(visited_row)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

to_search = [(start, current_direction_i)]
visited[start[0]][start[1]][current_direction_i] = 0

while to_search:
    (i, j), direction_i = to_search.pop(0)
    cost = visited[i][j][direction_i]
    for direction_di in range(-1, 3):
        new_direction_i = (direction_i + direction_di) % 4
        new_i = i + directions[new_direction_i][0]
        new_j = j + directions[new_direction_i][1]
        if grid[new_i][new_j] == '#':
            continue
        move_cost = 1 + abs(direction_di) * 1000
        new_cost = cost + move_cost
        if new_cost < visited[new_i][new_j][new_direction_i]:
            visited[new_i][new_j][new_direction_i] = new_cost
            to_search.append(((new_i, new_j), new_direction_i))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'E':
            end = (i, j)
print(visited[end[0]][end[1]])