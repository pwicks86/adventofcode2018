f = open("input.txt", "r")
coords = {}
coord_num = 1
limit = 10000

max_dim = -1
for l in f.readlines():
    x, y = map(int, l.split(","))
    max_dim = max(x,y,max_dim)
    coords[coord_num] = (x,y)
    coord_num += 1

w, h = max_dim + 1, max_dim + 1
field = [[0 for x in range(w)] for y in range(h)]

for y in range(h):
    for x in range(w):
        cur_point = field[y][x]
        for l, c in coords.items():
            cx, cy = c
            dist = abs(cx - x) + abs(cy - y)
            field[y][x] += dist
            if field[y][x] >= limit:
                break

total = 0
for y in range(h):
    for x in range(w):
        v = field[y][x]
        if v < limit:
            total += 1
print(total)
