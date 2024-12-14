from PIL import Image

robots = []

input_file = 'input.txt'
width = 101
height = 103
# seconds = 100

with open(input_file) as f:
    for line in f:
        p, v = tuple(a[2:] for a in line.strip().split())
        p = tuple(map(int, p.split(',')))
        v = tuple(map(int, v.split(',')))
        robots.append((p, v))

seconds = 0
while True:
    print(seconds)
    new_positions = []
    for r in robots:
        new_col = (r[0][0] + r[1][0] * seconds) % width
        new_row = (r[0][1] + r[1][1] * seconds) % height
        new_positions.append((new_col, new_row))

    pic = Image.new('1', (width, height))
    for p in new_positions:
        pic.putpixel(p, 1)
    pic.save(f'results/{seconds}.png')
    seconds += 1
