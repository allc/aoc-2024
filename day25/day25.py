schematics = []
with open('input.txt') as f:
    content = f.readlines()
    schematic = []
    for i in range(len(content)):
        if i % 8 < 7:
            schematic.append(content[i].strip())
        else:
            schematics.append(schematic)
            schematic = []
    schematics.append(schematic)

locks = []
keys = []

for schematic in schematics:
    o = []
    for i in range(len(schematic[0])):
        o.append([c[i] for c in schematic].count('#') - 1)
    if schematic[0][0] == '#':
        locks.append(o)
    else:
        keys.append(o)

print(locks)
print(keys)

def can_fit(lock, key):
    return all([a + b <= 5 for a, b in zip(lock, key)])

result = 0
for i in range(len(locks)):
    for j in range(len(keys)):
        if can_fit(locks[i], keys[j]):
            result += 1
print(result)
