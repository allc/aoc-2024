towels = []
patterns = []

with open('input.txt') as f:
    towels = list(f.readline().strip().split(', '))
    f.readline()
    patterns = list(line.strip() for line in f.readlines())

print(towels)
print(patterns)

def make_pattern(pattern, towels):
    dp = [0] * ((len(pattern)) + 1)
    dp[0] = 1
    for i in range(1, len(pattern) + 1):
        ways = 0
        for towel in towels:
            if towel == pattern[i - len(towel):i]:
                ways += dp[i - len(towel)]
        dp[i] = ways
    return dp[-1]

total = 0
for pattern in patterns:
    ways = make_pattern(pattern, towels)
    print(ways)
    total += ways
print(total)
