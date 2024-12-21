registers = [0] * 3 # register A, B, C
program = []

with open('input.txt') as f:
    for i in range(3):
        registers[i] = int(f.readline().strip()[12:])
    f.readline()
    program = list(map(int, f.readline().strip()[8:].split(',')))

print(registers)
print(program)

ip = 0

outs = []

def combo_oprand(oprand):
    if oprand <= 3:
        return oprand
    else:
        return registers[oprand - 4]
    
def adv(oprand):
    numerator = registers[0]
    denominator = 2 ** combo_oprand(oprand)
    registers[0] = numerator // denominator
    global ip
    ip += 2

def bxl(oprand):
    registers[1] = oprand ^ registers[1]
    global ip
    ip += 2

def bst(oprand):
    registers[1] = combo_oprand(oprand) & 0b111
    global ip
    ip += 2

def jnz(oprand):
    global ip
    if registers[0] == 0:
        ip += 2
        return
    ip = oprand

def bxc(oprand):
    registers[1] = registers[1] ^ registers[2]
    global ip
    ip += 2

def out(oprand):
    outs.append(combo_oprand(oprand) & 0b111)
    global ip
    ip += 2

def bdv(oprand):
    numerator = registers[0]
    denominator = 2 ** combo_oprand(oprand)
    registers[1] = numerator // denominator
    global ip
    ip += 2

def cdv (oprand):
    numerator = registers[0]
    denominator = 2 ** combo_oprand(oprand)
    registers[2] = numerator // denominator
    global ip
    ip += 2

operators = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while ip < len(program):
    operator = program[ip]
    oprand = program[ip + 1]
    operators[operator](oprand)

print(','.join(map(str, outs)))
