import operator
import re
f = open("input.txt", "r")
records = []
for l in f.readlines():
    records.append(l.strip().split("] ", 1))

records.sort(key=lambda i: i[0])
cur_guard = 0
guard_counts = {}
sleep_time = 0
for r in records:
    m = re.match("Guard #(\d+)|(falls asleep)|(wakes up)", r[1])
    m2 = re.match("\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})", r[0])
    time = int(m2.group(1))
    if m.group(1):
        cur_guard = int(m.group(1))
        if cur_guard not in guard_counts:
            guard_counts[cur_guard] = {m:0 for m in range(0, 60)}
        awake = True
    if m.group(2):
        sleep_time = time
    if m.group(3):
        for i in range(sleep_time, time):
            guard_counts[cur_guard][i] += 1

max_minutes = 0
max_minute = 0
max_guard = 0
for guard, counts in guard_counts.items():
    for m in range(0, 60):
        if counts[m] > max_minutes:
            max_guard = guard
            max_minute = m
            max_minutes = counts[m]

print(max_minute * max_guard)

