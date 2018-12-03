import re
f = open("input.txt", "r")
width, height = 2000, 2000
fab = [[0 for x in range(width)] for y in range(height)]
possibles = set()
for l in f.readlines():
    m = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", l.strip())
    sid,x,y,w,h = m.groups()
    possibles.add(sid)
    for i in range(int(w)):
        for j in range(int(h)):
            cur_f = fab[i+int(x)][j+int(y)]
            if cur_f != 0:
                possibles.discard(cur_f)
                possibles.discard(sid)
            fab[i+int(x)][j+int(y)] = sid
print(possibles.pop())

