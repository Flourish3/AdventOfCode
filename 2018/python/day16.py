#Advent of Code - Day 16

def isnum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# Addition
def addr(instr, registers):
    registers[instr[3]] = registers[instr[1]] + registers[instr[2]]
    return registers

def addi(instr, registers):
    registers[instr[3]] = registers[instr[1]]  + instr[2]
    return registers

# Multiplication
def mulr(instr, registers):
    registers[instr[3]] = registers[instr[1]] * registers[instr[2]]
    return registers

def muli(instr, registers):
    registers[instr[3]] = registers[instr[1]] * instr[2]
    return registers

# Bitwise AND
def banr(instr, registers):
    registers[instr[3]] = registers[instr[1]] & registers[instr[2]]
    return registers

def bani(instr, registers):
    registers[instr[3]] = registers[instr[1]] & instr[2]
    return registers

# Bitwise OR
def borr(instr, registers):
    registers[instr[3]] = registers[instr[1]] | registers[instr[2]]
    return registers

def bori(instr, registers):
    registers[instr[3]] = registers[instr[1]] | instr[2]
    return registers

# Assignment
def setr(instr, registers):
    registers[instr[3]] = registers[instr[1]]
    return registers

def seti(instr, registers):
    registers[instr[3]] = instr[1]
    return registers

# Greater-than testing
def gtir(instr, registers):
    registers[instr[3]] = 1 if instr[1] > registers[instr[2]] else 0
    return registers

def gtri(instr, registers):
    registers[instr[3]] = 1 if registers[instr[1]] > instr[2] else 0
    return registers

def gtrr(instr, registers):
    registers[instr[3]] = 1 if registers[instr[1]] > registers[instr[2]] else 0
    return registers

# Equality testing
def eqir(instr, registers):
    registers[instr[3]] = 1 if instr[1] == registers[instr[2]] else 0
    return registers

def eqri(instr, registers):
    registers[instr[3]] = 1 if registers[instr[1]] == instr[2] else 0
    return registers

def eqrr(instr, registers):
    registers[instr[3]] = 1 if registers[instr[1]] == registers[instr[2]] else 0
    return registers

class Sample():
    def __init__(self, before, after, inst):
        self.before =  before
        self.after = after
        self.inst = inst

def execute(registers, instructions, opCodes):
    for i in instructions:
        registers = opCodes[i[0]](i, registers)

    return registers

def part1(samples):
    three = 0
    instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    for s in samples:
        equalCount = 0
        for i in instructions:
            if i(s.inst, s.before.copy()) == s.after:
                equalCount += 1

        if equalCount >= 3:
            three += 1
    return three

def part2(samples, exampleProgram):
    opCodes = {}

    instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    # Figure out which index is which opCode
    while len(opCodes) < 16:
        for s in samples:
            missingIdxs = []
            for c,i in enumerate(instructions):
                if i(s.inst, s.before.copy()) == s.after:
                    missingIdxs.append(c)

            if len(missingIdxs) == 1:
                if s.inst[0] not in opCodes:
                    opCodes[s.inst[0]] = instructions[missingIdxs[0]]
            else:
                missing = 0
                missInstIdx = 0
                for i in missingIdxs:
                    if instructions[i] not in opCodes.values():
                        missing += 1
                        missInstIdx = i

                if missing == 1:
                    opCodes[s.inst[0]] = instructions[missInstIdx]
    regs = execute([0,0,0,0], exampleProgram, opCodes)

    return regs[0]

def main():

    samples = []
    exampleProgram = []

    with open("../data/input16.txt") as f:
        newCount = 0
        sampling = True
        for line in f.readlines():
            if sampling:
                line = line.split(": ")

                if line[0] == "Before":
                    before = [int(c) for c in list(line[1].strip()) if isnum(c)]
                elif line[0] == "After":
                    after = [int(c) for c in list(line[1].strip()) if isnum(c)]
                    samples.append(Sample(before, after, inst))
                elif line[0] != "\n":
                    inst = list(map(int,line[0].split(" ")))
                else:
                    newCount += 1

                if line[0] != "\n":
                    newCount = 0

                if newCount > 2:
                    sampling = False

            else:
                if line != "\n":
                    exampleProgram.append(list(map(int,line.strip().split(" "))))

    print("Part 1: {}".format(part1(samples)))
    print("Part 2: {}".format(part2(samples, exampleProgram)))

main()
