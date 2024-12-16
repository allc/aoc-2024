grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
for i, row in enumerate(grid):
    print(f'{i:02}', ''.join(row))

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
        visited_block = []
        visited_row.append([float('inf')] * 4)
    visited.append(visited_row)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

to_search = [(start, current_direction_i)]
visited[start[0]][start[1]][current_direction_i] = 0

while to_search:
    (i, j), direction_i = to_search.pop(0)
    cost = visited[i][j][direction_i]
    for direction_di in range(-1, 2):
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
for i, row in enumerate(visited):
    print(i, row)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'E':
            end = (i, j)

# trace back
i, j = end
cost = min(visited[i][j])
direction_i = visited[i][j].index(cost)
ends = [(end, direction_i)]
backtrace_visited = [[[False] * 4 for _ in range(len(grid[i]))] for i in range(len(grid))]
while ends:
    end, direction_i = ends.pop(0)
    i, j = end
    cost = visited[i][j][direction_i]
    while (i, j) != start:
        grid[i][j] = 'O'
        if backtrace_visited[i][j][direction_i]:
            break
        backtrace_visited[i][j][direction_i] = True
        print(f'{i = }, {j = }, {direction_i = }, {cost = }')
        last_i = i - directions[direction_i][0]
        last_j = j - directions[direction_i][1]
        last_direction_is = []
        for last_direction_i in range(4):
            if visited[last_i][last_j][last_direction_i] + 1 + 1000 * ((direction_i - last_direction_i) % 2) == cost:
                last_direction_is.append(last_direction_i)
        last_direction_i = last_direction_is[0]
        for last_direction_i_ in last_direction_is:
            ends.append(((last_i, last_j), last_direction_i_))
        i, j = last_i, last_j
        direction_i = last_direction_i
        cost = visited[i][j][direction_i]
    
for i, row in enumerate(grid):
    print(f'{i:02}', ''.join(row))

count = 0
for row in grid:
    count += row.count('O')
print(count + 1)
