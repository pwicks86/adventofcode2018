from string import ascii_lowercase

f = open("input.txt", "r")
poly = []
inlist = [ord(c) for c in f.read().strip()]
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

def find_len(seq):
    global poly
    poly = seq
    while True:
        if not compress():
            break
    return len(poly)


minlen = 999999999999999999999999999
for c in ascii_lowercase:
    low_o = ord(c)
    up_o = ord(c.upper())
    l = [i for i in inlist if i != low_o and i != up_o]
    clen = find_len(l)
    minlen = min(minlen, clen)

print(minlen)

