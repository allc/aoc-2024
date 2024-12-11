stones = list(map(int, input().split()))
print(stones)

def blink(s):
    result = []
    if s == 0:
        result.append(1)
    elif len(str(s)) % 2 == 0:
        result.append(int(str(s)[:len(str(s))//2]))
        result.append(int(str(s)[len(str(s))//2:]))
    else:
        result.append(s * 2024)
    return result

blink_results = dict() # (stone, blinks) -> number of stones

def blink_n_times(s, n):
    if n == 0:
        return 1
    if (s, n) in blink_results:
        return blink_results[(s, n)]
    stones = blink(s)
    result = 0
    for stone in stones:
        result += blink_n_times(stone, n - 1)
    blink_results[(s, n)] = result
    return result

result = 0
for s in stones:
    result += blink_n_times(s, 75)
print(result)
