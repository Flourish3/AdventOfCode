#Advent of Code - Day 03

from collections import defaultdict

def parse(line):
    ids, _, offset, d = line.split()
    left, top = offset[:-1].split(",")
    width, height = d.split("x")
    return ids, int(left), int(top), int(width), int(height)

lines = [l.strip() for l in open("../data/input03.txt").readlines()]

fabric = defaultdict(int)
overlapping = 0

data = [parse(line) for line in lines]

for _, l, t, w, h in data:
    for i in range(w):
        for j in range(h):
            fabric[(i + l, j + t)] += 1

for v in fabric.values():
    if v > 1:
        overlapping += 1

print("Part 1: {}".format(overlapping))

for ids, l, t, w, h in data:
    isValid = True
    for i in range(w):
        for j in range(h):
            if fabric[(i + l, j + t)] != 1:
                isValid = False
                break
        if not isValid:
            break
    if isValid:
        # Part 2
        print("Part 2: {}".format(ids[1:]))