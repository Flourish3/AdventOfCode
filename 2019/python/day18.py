# Advent of code - Day 18

lines = [l.strip() for l in open("../data/input18.txt").readlines()]
caveMap = []
y = 0
for l in lines:
    x=0
    for c in list(l):
        caveMap[(x,y)] = c
        x += 1
    y += 1
