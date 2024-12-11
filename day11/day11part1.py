stones = list(map(int, input().split()))
print(stones)

def blink(stones):
    result = []
    for s in stones:
        if s == 0:
            result.append(1)
        elif len(str(s)) % 2 == 0:
            result.append(int(str(s)[:len(str(s))//2]))
            result.append(int(str(s)[len(str(s))//2:]))
        else:
            result.append(s * 2024)
    return result

for i in range(10):
    stones = blink(stones)
    print(i, len(stones), stones)