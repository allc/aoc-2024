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

for game in games:
    button_a, button_b, prize = game
    button_b_times = prize[0] // button_b[0]
    min_cost = float('inf')
    for i in range(button_b_times, -1, -1):
        x_left = prize[0] - i * button_b[0]
        y_left = prize[1] - i * button_b[1]
        if x_left % button_a[0] == 0:
            button_a_times = x_left // button_a[0]
            if y_left == button_a_times * button_a[1]:
                cost = button_a_times * 3 + i
                min_cost = min(min_cost, cost)
    if min_cost != float('inf'):
        result += min_cost

print(result)