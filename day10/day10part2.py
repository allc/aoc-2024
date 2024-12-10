with open('input.txt') as f:
    grid = [list(map(int, l.strip())) for l in f.read().splitlines()]

score = [[0] * len(grid[0]) for _ in range(len(grid))]

neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 9:
            score[i][j] = 1

for n in range(8, -1, -1):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == n:
                for di, dj in neighbours:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                        if grid[i + di][j + dj] == n + 1:
                            score[i][j] += score[i + di][j + dj]
    for row in score:
        print(row)
    print()

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            result += score[i][j]
print(result)