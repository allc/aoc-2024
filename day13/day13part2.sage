games = []
with open('input.txt') as f:
    for line in f:
        if line.startswith('Button A'):
            line = line.split(': ')[1]
            line = line.split(', ')
            x = int(line[0][2:])
            y = int(line[1][2:])
            button_a = (x, y)
        elif line.startswith('Button B'):
            line = line.split(': ')[1]
            line = line.split(', ')
            x = int(line[0][2:])
            y = int(line[1][2:])
            button_b = (x, y)
        elif line.startswith('Prize'):
            line = line.split(': ')[1]
            line = line.split(', ')
            x = int(line[0][2:])
            y = int(line[1][2:])
            prize = (x, y)
            games.append((button_a, button_b, prize))

print(games)

result = 0
add_c = 10000000000000

for game in games:
    button_a, button_b, prize = game
    x1, y1 = button_a
    x2, y2 = button_b
    prize = (prize[0] + add_c, prize[1] + add_c)

    var('a b')
    solution = solve([a * x1 + b * x2 == prize[0], a * y1 + b * y2 == prize[1]], a, b)
    assert len(solution) == 1 # we got lucky, all games have a unique solution (integer or not)
    a, b = map(lambda x: x.rhs().n(), solution[0])
    if a.is_integer() and b.is_integer():
        result += 3 * a + b
print(int(result))