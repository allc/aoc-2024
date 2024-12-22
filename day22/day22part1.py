with open('input.txt') as f:
    secret_numbers = list(map(int, f.read().splitlines()))
print(secret_numbers)

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

result = 0
for n in secret_numbers:
    for i in range(2000):
        n = get_next_secret_number(n)
    result += n
print(result)
