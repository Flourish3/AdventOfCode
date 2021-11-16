# Advent of code - day 25
# Advent of code - day21

# Advent of code - Day 17

from intcode import *

inp = [int(ins) for ins in open("../data/input25.txt").read().split(",")]


def part1():
    machine = Machine([j for j in inp])

    instr = []
    outs = []

    while True:
        try:
            machine.run_machine(instr)
        except Output as e:
            outs.append(e.output)
        except Interrupt:
            print("".join([chr(o) for o in outs if o < 0x110000]))
            break

        if len(outs) >= 9 and "".join([chr(c) for c in outs[-9:]]) == "Command?\n":
            print("".join([chr(o) for o in outs if o < 0x110000]))
            inputCommand = input("Give command:")
            instr = list(map(lambda x: ord(x), list(inputCommand + "\n")))
            outs = []

#Fixed point, sand, space law space, wreath
