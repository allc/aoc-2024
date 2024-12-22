with open('input.txt') as f:
    secret_numbers = list(map(int, f.read().splitlines()))

def mix_and_prune(secret_number, n):
    n = n ^ secret_number
    return n % 16777216

def get_next_secret_number(secret_number):
    n = secret_number
    n_ = n * 64
    n = mix_and_prune(n, n_)
    n_ = n // 32
    n = mix_and_prune(n, n_)
    n_ = n * 2048
    n = mix_and_prune(n, n_)
    return n

sequences = []
for n in secret_numbers:
    sequence = [n % 10]
    for i in range(2000):
        n = get_next_secret_number(n)
        sequence.append(n % 10)
    sequences.append(sequence)

from collections import defaultdict
changes_to_price= defaultdict(int)
for sequence in sequences:
    changes = set()
    for i in range(4, len(sequence)):
        change_sequence = tuple(a - b for a, b in zip(sequence[i - 3: i + 1], sequence[i - 4: i]))
        if change_sequence in changes:
            continue
        changes.add(change_sequence)
        changes_to_price[change_sequence] += sequence[i]
print(max(changes_to_price.values()))
