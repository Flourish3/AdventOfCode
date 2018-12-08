#Advent of Code - Day 02
from collections import Counter

lines = [l.strip() for l in open("../data/input02.txt").readlines()]

c = [0,0]

for l in lines:
    occurences = [b for a,b in Counter(l).most_common()]
    if 2 in occurences:
        c[0] += 1
    if 3 in occurences:
        c[1] += 1
print("Part 1: {}".format(c[0]*c[1]))

found = False
for i in lines:
    for j in lines:
        diff = 0
        for a,b in zip(list(j),list(i)):
            if a != b:
                diff += 1
        if diff == 1 and not found:
            found = True
            res = [a for a,b in zip(list(j),list(i)) if a==b]
            print("Part 2: {}".format("".join(res)))