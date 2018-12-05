f = open("input.txt", "r")
poly = [ord(c) for c in f.read().strip()]
print(poly)
start_index = 0

def compress():
    global poly
    global start_index
    if len(poly) % 1000 == 0:
        print(len(poly))
    for i in range(start_index, len(poly) - 1):
        pair = poly[i:i+2]
        if abs(pair[0] - pair[1]) == 32:
            poly = poly[:i] + poly[i+2:]
            return True
    return False

while True:
    if not compress():
        break

print(len(poly))
