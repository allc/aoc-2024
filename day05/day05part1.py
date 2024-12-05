from collections import defaultdict

page_ordering_rules_after = defaultdict(list)
page_ordering_rules_before = defaultdict(list)

def check_ordering(page_ordering_rules_after, page_ordering_rules_before, page_ordering):
    for i in range(len(page_ordering) - 1):
        for j in range(i + 1, len(page_ordering)):
            if page_ordering[i] in page_ordering_rules_after[page_ordering[j]]:
                return False
            if page_ordering[j] in page_ordering_rules_before[page_ordering[i]]:
                return False
    return True

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        parts = line.split('|')
        page_ordering_rules_after[parts[0]].append(parts[1])
        page_ordering_rules_before[parts[1]].append(parts[0])
    print(page_ordering_rules_after)
    print(page_ordering_rules_before)

    correct = []
    for line in f:
        line = line.strip()
        update = line.split(',')
        if check_ordering(page_ordering_rules_after, page_ordering_rules_before, update):
            correct.append(update)
    print(correct)

    result = 0
    for c in correct:
        result += int(c[len(c) // 2])
    print(result)