import re
f = open("input.txt", "r")
width, height = 2000, 2000
fab = [[0 for x in range(width)] for y in range(height)]
for l in f.readlines():
    m = re.match("#\d+ @ (\d+),(\d+): (\d+)x(\d+)", l.strip())
    x,y,w,h = m.groups()
    for i in range(int(w)):
        for j in range(int(h)):
            fab[i+int(x)][j+int(y)] += 1

t = 0
for i in range(width):
    for j in range(height):
        if fab[i][j] > 1:
            t += 1

print(t)
