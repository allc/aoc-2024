from collections import defaultdict
with open('input.txt') as f:
    garden = [list(line.strip()) for line in f]
print(garden)


count_area = defaultdict(int)
edges = defaultdict(set)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

garden_visited = [[False for _ in range(
    len(garden[i]))] for i in range(len(garden))]


def visit_garden(x, y, garden, garden_visited, key):
    letter = garden[x][y]
    count_area[key] += 1
    garden_visited[x][y] = True
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_y < 0 or new_x >= len(garden) or new_y >= len(garden[x]):
            edges[key].add((direction, x, y))
            continue
        if garden[new_x][new_y] != letter:
            edges[key].add((direction, x, y))
            continue
        if not garden_visited[new_x][new_y]:
            visit_garden(new_x, new_y, garden, garden_visited, key)


key = 0
for i in range(0, len(garden)):
    for j in range(0, len(garden[i])):
        if not garden_visited[i][j]:
            visit_garden(i, j, garden, garden_visited, key)
            key += 1


sides = defaultdict(int)
for key in edges:
    while edges[key]:
        sides[key] += 1
        edge = edges[key].pop()
        direction = edge[0]
        x, y = edge[1], edge[2]
        dx = direction[1]
        dy = direction[0]
        x_ = x + dx
        y_ = y + dy
        while (direction, x_, y_) in edges[key]:
            edges[key].remove((direction, x_, y_))
            x_ += dx
            y_ += dy
        x_ = x - dx
        y_ = y - dy
        while (direction, x_, y_) in edges[key]:
            edges[key].remove((direction, x_, y_))
            x_ -= dx
            y_ -= dy
print(sides)


result = 0
for key in count_area:
    result += count_area[key] * sides[key]

print(count_area)

print(result)
