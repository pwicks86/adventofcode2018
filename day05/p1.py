f = open("input.txt", "r")
poly = [c for c in f.read().strip()]
print(poly)
start_index = 0

def compress():
    global poly
    global start_index
    print(len(poly))
    for i in range(start_index, len(poly) - 1):
        pair = poly[i:i+2]
        if pair[0] != pair[1] and pair[0].lower() == pair[1].lower():
            poly = poly[:i] + poly[i+2:]
            return True
    return False

while True:
    if not compress():
        break

print(len(poly))
