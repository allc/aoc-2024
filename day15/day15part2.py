def count_num_boxes(warehouse):
    count = 0
    for row in warehouse:
        count += row.count('[')
    return count

warehouse = []
movements = []

input_to_warehouse = {
    '#': '##',
    '.': '..',
    'O': '[]',
    '@': '@.',
}

with open('input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        warehouse_row = []
        for char in line.strip():
            warehouse_row.extend(input_to_warehouse[char])
        warehouse.append(warehouse_row)

    for line in f:
        movements.extend(list(line.strip()))
        
print(warehouse)
print(movements)

print('Number of boxes:', count_num_boxes(warehouse))

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
    
    x, y = start
    if warehouse[x + dx][y + dy] == '#':
        return start
    if warehouse[x + dx][y + dy] == '.':
        warehouse[x + dx][y + dy] = '@'
        warehouse[x][y] = '.'
        return (x + dx, y + dy)
    
    boxes_to_move = []
    boxes_to_check = []
    if warehouse[x + dx][y + dy] == '[':
        boxes_to_check.append((x + dx, y + dy))
    if warehouse[x + dx][y + dy] == ']':
        boxes_to_check.append((x + dx, y + dy - 1))
    
    while boxes_to_check:
        x, y = boxes_to_check.pop(0)
        boxes_to_move.append((x, y))
        if warehouse[x + dx][y + dy] == '#':
            return start
        
        if direction == '^' or direction == 'v':
            if warehouse[x + dx][y + dy + 1] == '#':
                return start
            if warehouse[x + dx][y + dy] == '[':
                boxes_to_check.append((x + dx, y + dy))
            if warehouse[x + dx][y + dy] == ']':
                boxes_to_check.append((x + dx, y + dy - 1))
            if warehouse[x + dx][y + dy + 1] == '[':
                boxes_to_check.append((x + dx, y + dy + 1))

        if direction == '<':
            if warehouse[x + dx][y + dy] == ']':
                boxes_to_check.append((x + dx, y + dy - 1))

        if direction == '>':
            if warehouse[x + dx][y + dy + 1] == '#':
                return start
            if warehouse[x + dx][y + dy + 1] == '[':
                boxes_to_check.append((x + dx, y + dy + 1))

    boxes_to_move.reverse()
    for x, y in boxes_to_move:
        warehouse[x][y] = '.'
        warehouse[x][y + 1] = '.'
        warehouse[x + dx][y + dy] = '['
        warehouse[x + dx][y + dy + 1] = ']'
    x, y = start
    warehouse[x + dx][y + dy] = '@'
    warehouse[x][y] = '.'

    return x + dx, y + dy

for movement in movements:
    start = move(warehouse, start, movement)
    # for row in warehouse:
    #     print(''.join(row))
    # print()

result = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '[':
            result += i * 100 + j
print(result)

print('Number of boxes:', count_num_boxes(warehouse))
