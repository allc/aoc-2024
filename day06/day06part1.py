world = []
with open('input.txt') as f:
    for line in f:
        world.append(list(line.strip()))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
facing_mapping = {'^': 0, '>': 1, 'v': 2, '<': 3}

i = 0
j = 0
facing = -1
# find guard location and facing
for i in range(len(world)):
    for j in range(len(world[i])):
        if world[i][j] in facing_mapping:
            facing = facing_mapping[world[i][j]]
            break
    if facing != -1:
        break

print(f'Guard at {i}, {j} facing {facing}')

world[i][j] = 'X'
while True:
    direction = directions[facing]
    i_ = i + direction[0]
    j_ = j + direction[1]
    if i_ < 0 or i_ >= len(world) or j_ < 0 or j_ >= len(world[i_]):
        break
    if world[i_][j_] == '#':
        facing = (facing + 1) % 4
        continue
    i = i_
    j = j_
    world[i][j] = 'X'

result = 0
for row in world:
    result += row.count('X')

print(result)