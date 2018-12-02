f = open("input.txt", "r")
freqs = [int(l) for l in f.readlines()]
print(sum(freqs))
