from collections import Counter
from itertools import product
f = open("input.txt", "r")
codes = [l.strip() for l in f.readlines()]
for c1, c2 in product(codes, codes):
    if c1 == c2:
        continue
    diff_count = 0
    diff_index = 0
    for index, cs in enumerate(zip(c1, c2)):
        c1c, c2c = cs
        if c1c != c2c:
            diff_count += 1
            diff_index = index
    if diff_count == 1:
        common = c1[:diff_index] + c1[diff_index+1:]
        print(common)
        break
