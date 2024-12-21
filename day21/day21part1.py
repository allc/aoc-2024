codes = []
with open('input.txt') as f:
    for line in f:
        codes.append(line.strip())
print(codes)

class Keypad:
    def find_coordinate(self, key):
        for i in range(len(self.keypad)):
            for j in range(len(self.keypad[i])):
                if self.keypad[i][j] == key:
                    return i, j

class NumericKeypad(Keypad):
    def __init__(self):
        self.keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
        self.row = 3
        self.col = 2

    def find_sequences(self, code):
            sequences = []
            for key in code:
                key_sequences = []
                i, j = self.find_coordinate(key)
                vertical = i - self.row
                horizontal = j - self.col
                if vertical > 0:
                    vertical_sequence = 'v' * vertical
                else:
                    vertical_sequence = '^' * abs(vertical)
                if horizontal > 0:
                    horizontal_sequence = '>' * horizontal
                else:
                    horizontal_sequence = '<' * abs(horizontal)

                if key in ['1', '4', '7'] and self.keypad[self.row][self.col] in ['0', 'A']:
                    key_sequences.append(vertical_sequence + horizontal_sequence + 'A')
                elif key in ['0', 'A'] and self.keypad[self.row][self.col] in ['1', '4', '7']:
                    key_sequences.append(horizontal_sequence + vertical_sequence + 'A')
                else:
                    key_sequences.append(vertical_sequence + horizontal_sequence + 'A')
                    if horizontal_sequence and vertical_sequence:
                        key_sequences.append(horizontal_sequence + vertical_sequence + 'A')
                self.row = i
                self.col = j
                sequences.append(key_sequences)
            return sequences

class DirectionalKeypad(Keypad):
    def __init__(self):
        self.keypad = [[None, '^', 'A'], ['<', 'v', '>']]
        self.row = 0
        self.col = 2

    def find_sequences(self, code):
            sequences = []
            for key in code:
                key_sequences = []
                i, j = self.find_coordinate(key)
                vertical = i - self.row
                horizontal = j - self.col
                if vertical > 0:
                    vertical_sequence = 'v' * vertical
                else:
                    vertical_sequence = '^' * abs(vertical)
                if horizontal > 0:
                    horizontal_sequence = '>' * horizontal
                else:
                    horizontal_sequence = '<' * abs(horizontal)

                if (i, j) == (1, 0):
                    key_sequences.append(vertical_sequence + horizontal_sequence + 'A')
                elif (self.row, self.col) == (1, 0):
                    key_sequences.append(horizontal_sequence + vertical_sequence + 'A')
                else:
                    key_sequences.append(horizontal_sequence + vertical_sequence + 'A')
                    key_sequences.append(vertical_sequence + horizontal_sequence + 'A')
                self.row = i
                self.col = j
                sequences.append(key_sequences)
            return sequences

numeric_keypad = NumericKeypad()
directional_keypad = DirectionalKeypad()

mem = dict()

def find_min_sequence_length_(sequence, r):
    if (sequence, r) in mem:
        return mem[(sequence, r)]
    if r == 0:
        return len(sequence)
    sequences = directional_keypad.find_sequences(sequence)
    min_sequence_length = 0
    for sequences_ in sequences:
        if len(sequences_) == 1:
            min_sequence_length += find_min_sequence_length_(sequences_[0], r - 1)
        else:
            min_sequence_length += min(find_min_sequence_length_(sequence, r - 1) for sequence in sequences_)
    mem[(sequence, r)] = min_sequence_length
    return min_sequence_length

def find_min_sequence_length(code, r):
    sequences = numeric_keypad.find_sequences(code)
    min_sequence_length = 0
    for sequences_ in sequences:
        if len(sequences_) == 1:
            min_sequence_length += find_min_sequence_length_(sequences_[0], r)
        else:
            min_sequence_length += min(find_min_sequence_length_(sequence, r) for sequence in sequences_)
    return min_sequence_length

result = 0
for code in codes:
    min_sequence_length = find_min_sequence_length(code, 2)
    print(min_sequence_length)
    result += min_sequence_length * int(code[:3])
print(result)
