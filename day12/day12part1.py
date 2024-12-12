with open('input.txt') as f:
    garden = [list(line.strip()) for line in f]
print(garden)

from collections import defaultdict

count_area = defaultdict(int)
count_diameter = defaultdict(int)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

garden_visited = [[False for _ in range(len(garden[i]))] for i in range(len(garden))]

def visit_garden(x, y, garden, garden_visited, key):
    letter = garden[x][y]
    count_area[key] += 1
    garden_visited[x][y] = True
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_y < 0 or new_x >= len(garden) or new_y >= len(garden[x]):
            count_diameter[key] += 1
            continue
        if garden[new_x][new_y] != letter:
            count_diameter[key] += 1
            continue
        if not garden_visited[new_x][new_y]:
            visit_garden(new_x, new_y, garden, garden_visited, key)

key = 0
for i in range(0, len(garden)):
    for j in range(0, len(garden[i])):
       if not garden_visited[i][j]:
           visit_garden(i, j, garden, garden_visited, key)
           key += 1 

result = 0
for key in count_area:
    result += count_area[key] * count_diameter[key]

print(count_area)
print(count_diameter)

print(result)
