#Advent of Code - Day 01

from itertools import cycle, accumulate

with open("../data/input01.txt") as f:

    changes = [int(n.strip()) for n in f.readlines()]
    print("Part 1: {}".format(sum(changes)))

    seen = set()
    print("Part 2: {}".format(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))))