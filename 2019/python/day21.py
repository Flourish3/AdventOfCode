# Advent of code - day21

# Advent of code - Day 17

from intcode import *

inp = [int(ins) for ins in open("../data/input21.txt").read().split(",")]

springScriptP1 = """NOT B J
NOT C T
OR T J
AND D J
NOT A T
OR T J
WALK
"""

springScriptP2 = """NOT B J
NOT C T
OR T J
AND D J
NOT A T
OR T J
RUN
"""

def part1():
    machine = Machine([j for j in inp])
    grid = {}
    output_type = 0
    x,y = 0,0
    instr = [ord(c) for c in list(springScriptP1)]
    outs = []

    while True:
        try:
            machine.run_machine(instr)
        except Output as e:
            outs.append(e.output)
        except Interrupt:
            break

    print("".join([chr(o) for o in outs if o < 0x110000]))
    return outs[-1]

def part2():
    machine = Machine([j for j in inp])
    grid = {}
    output_type = 0
    x,y = 0,0
    instr = [ord(c) for c in list(springScriptP2)]
    outs = []

    while True:
        try:
            machine.run_machine(instr)
        except Output as e:
            outs.append(e.output)
        except Interrupt:
            break

    print("".join([chr(o) for o in outs if o < 0x110000]))
    return outs[-1]

print("Part 1: {}".format(part1()))

print("Part 2: {}".format(part2()))