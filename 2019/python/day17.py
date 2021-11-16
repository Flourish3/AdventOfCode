# Advent of code - Day 17

from intcode import *

inp = [int(ins) for ins in open("../data/input17.txt").read().split(",")]


def part1():
    machine = Machine([j for j in inp])
    grid = {}
    output_type = 0
    x,y = 0,0

    while True:
        try:
            machine.run_machine([])
        except Output as e:
            print(e.output)
            pass 
          
        except Interrupt:
            break

    return len([v for v in grid.values() if v == "O"])

print("Part 1: {}".format(part1()))

#print("Part 2: {}".format(part2()))