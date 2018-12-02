from collections import Counter
f = open("input.txt", "r")
codes = f.readlines()
two_count = 0
three_count = 0
for code in codes:
    c = Counter(code)
    counts = set(c.values())
    if 2 in counts:
        two_count += 1
    if 3 in counts:
        three_count +=1

print(two_count * three_count)

