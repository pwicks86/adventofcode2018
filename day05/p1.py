f = open("input.txt", "r")
poly = [ord(c) for c in f.read().strip()]
start_index = 0

def compress():
    global poly
    global start_index
    i = 0
    did_swap = False
    while i < len(poly) - 1:
        pair = poly[i:i+2]
        if abs(pair[0] - pair[1]) == 32:
            poly = poly[:i] + poly[i+2:]
            did_swap = True
            i = max(0, i - 1)
        else:
            i += 1
    return did_swap

while True:
    if not compress():
        break

print(len(poly))
