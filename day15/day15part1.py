warehouse = []
movements = []

with open('input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        warehouse.append(list(line.strip()))

    for line in f:
        movements.extend(list(line.strip()))
        
print(warehouse)
print(movements)

# Find the starting position
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '@':
            start = (i, j)
            break
print(f'Starting position: {start}')

def move(warehouse, start, direction):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }
    dx, dy = directions[direction]
    
    # Scan direction
    x, y = start
    x_, y_ = x, y
    while True:
        x_ += dx
        y_ += dy
        # assume warehouse is bounded by wall, so no need to check for out of bounds
        if warehouse[x_][y_] == '#':
            break
        if warehouse[x_][y_] == '.':
            break
        if warehouse[x_][y_] == 'O':
            continue

    if warehouse[x_][y_] == '#':
        return start
    
    warehouse[x_][y_] = warehouse[x + dx][y + dy]
    warehouse[x + dx][y + dy] = '@'
    warehouse[x][y] = '.'
    return (x + dx, y + dy)

for movement in movements:
    start = move(warehouse, start, movement)
    for row in warehouse:
        print(''.join(row))
    print()

result = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == 'O':
            result += i * 100 + j
print(result)
