from collections import defaultdict
f = open("input.txt", "r")
freqs = [int(l) for l in f.readlines()]
freq_dict = defaultdict(int)
freq_dict[0] = 1
cur_freq = 0
done = False
while True:
    for f in freqs:
        cur_freq += f
        freq_dict[cur_freq] += 1
        if freq_dict[cur_freq] == 2:
            print(cur_freq)
            done = True
            break
    if done:
        break
