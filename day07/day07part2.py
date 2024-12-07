equations = []

with open('input.txt') as f:
    for line in f:
        line = line.strip().split(': ')
        target = int(line[0])
        elements = list(map(int, line[1].split()))
        equations.append((target, elements))
print(equations)

def check(current, elements, target):
    if len(elements) == 0:
        return current == target
    if current > target:
        return False
    return any([check(current + elements[0], elements[1:], target), check(current * elements[0], elements[1:], target), check(int(str(current) + str(elements[0])), elements[1:], target)])
result = 0

for target, elements in equations:
    if check(0, elements, target):
        result += target
print(result)
