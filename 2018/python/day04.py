#Advent of Code - Day 04

from collections import defaultdict

time = defaultdict(lambda: [0]*60)

with open("../data/input04.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    lines.sort()

lastFall = 0
lastId = 0
for line in lines:
    line = line.split()
    print(line)
    if line[2] == 'Guard':
        lastId = line[3][1:]
    elif line[2] == 'falls':
        lastFall = int(line[1][-3:-1])
    elif line[2] == 'wakes':
        wake = int(line[1][-3:-1])
        for i in range(lastFall,wake):
            time[lastId][i] += 1

maxSleep = 0
ans = 0
for k,v in time.items():
    sleep = sum(v)

    if sleep > maxSleep:
        maxSleep = sleep
        ans = int(k)*v.index(max(v))

maxFreq = 0
ans2 = 0
for k,v in time.items():
    maxV = max(v)
    if maxV > maxFreq:
        maxFreq = maxV
        ans2 = int(k)*v.index(maxV)



print("Part 1: {}".format(ans))
print("Part 2: {}".format(ans2))

