towels = []
patterns = []

with open('input.txt') as f:
    towels = list(f.readline().strip().split(', '))
    f.readline()
    patterns = list(line.strip() for line in f.readlines())

print(towels)
print(patterns)

def make_pattern(pattern, towels):
    dp = [False] * ((len(pattern)) + 1)
    dp[0] = True
    for i in range(1, len(pattern) + 1):
        for towel in towels:
            if towel == pattern[i - len(towel):i]:
                if dp[i - len(towel)]:
                    dp[i] = True
                    break
    return dp[-1]

count = 0
for pattern in patterns:
    if make_pattern(pattern, towels):
        count += 1
print(count)