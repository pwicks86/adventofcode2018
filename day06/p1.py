from collections import Counter
f = open("input.txt", "r")
# f = open("test.txt", "r")
coords = {}
coord_num = 1

max_dim = -1
for l in f.readlines():
    x, y = map(int, l.split(","))
    max_dim = max(x,y,max_dim)
    coords[coord_num] = (x,y)
    coord_num += 1

w, h = max_dim + 1, max_dim + 1
field = [[0 for x in range(w)] for y in range(h)]

for l, c in coords.items():
    x, y = c
    field[y][x] = l

for y in range(h):
    for x in range(w):
        # print(f"{x},{y}")
        # import pdb; pdb.set_trace()
        cur_point = field[y][x]
        if cur_point != 0:
            continue
        min_dist = 9999999999999
        min_c = None
        min_dist_count = 0
        for l, c in coords.items():
            cx, cy = c
            dist = abs(cx - x) + abs(cy - y)
            if dist < min_dist:
                min_dist = dist
                min_c = l
                min_dist_count = 1
            elif dist == min_dist:
                min_dist_count += 1
        if min_dist_count == 1:
            field[y][x] = min_c
        else:
            field[y][x] = "."

bad_set = set()
for y in range(h):
    bad_set.add(field[y][0])
    bad_set.add(field[y][w-1])

for x in range(w):
    bad_set.add(field[0][x])
    bad_set.add(field[h-1][x])

bad_set.remove(".")
counts = Counter()
for y in range(h):
    for x in range(w):
        v = field[y][x]
        if v not in bad_set and v != ".":
            counts[v] += 1

print(counts.most_common(1)[0][1])

# for x in range(w):
    # for y in range(h):
        # print(field[x][y], end="")
    # print()
