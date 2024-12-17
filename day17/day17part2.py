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

def out(oprand): # operator 5
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

# program: [2, 4, 1, 6, 7, 5, 4, 6, 1, 4, 5, 5, 0, 3, 3, 0]
# 2, 4: B = A & 0b111
# 1, 6: B = B ^ 0b110
# 7, 5: C = A >> B
# 4, 6: B = B ^ C
# 1, 4: B = B ^ 0b100
# 5, 5: out B & 0b111
# 0, 3: A = A >> 3
# 3, 0: if A != 0: ip = 0


program_ = list(reversed(program))
possible = [(0, 0)]
while possible:
    A, i = possible.pop(0)
    A <<= 3
    for b in range(8):
        A_ = A + b
        b_ = b ^ 0b110
        c = A_ >> b_
        b_ = b_ ^ c
        b_ = b_ ^ 0b100
        if b_ & 0b111 == program_[i]:
            if i == len(program_) - 1:
                print(A_)
                exit()
            possible.append((A_, i + 1))                          
