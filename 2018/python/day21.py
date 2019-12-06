# Advent of code - Day 21

# Advent of code - Day 19
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

def execute(registers, ip, program, instructions):
    count = 0
    regsVals = {}
    oldRegThree = 0
    while registers[ip] < len(program):
        currentInstruction = program[registers[ip]]
        registers = instructions[currentInstruction[0]](currentInstruction, registers)
        registers[ip] += 1
        if registers[ip] == 28:
            if registers[3] not in regsVals:
                regsVals[count] = (registers[3])
                count += 1
                break

    return registers, count

def part1(ip, program, instructions):

    registers,_ = execute([0,0,0,0,0,0], ip, program, instructions)

    return registers[3]

def part2():
    d = 0
    s = set()
    foundLast = False
    lastReg3 = 0
    while True:
        b = d | 0x10000
        d = 9450265
        while True:
            e = b & 0xFF
            d += e
            d &= 0xFFFFFF
            d *= 65899
            d &= 0xFFFFFF
            if (256 > b):
                if d not in s:
                    #print(d)
                    s.add(d)
                    lastReg3 = d
                else:
                    foundLast = True
                break
            # the following code was the optimised part
            b = b // 256
        if foundLast:
            break
    return lastReg3


def main():
    ip = 0
    program = []

    intructions = {}
    instructionNames = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    instructionFunctions= [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    for name,instr in zip(instructionNames, instructionFunctions):
        intructions[name] = instr

    with open("../data/input21.txt") as f:
        for l in f.readlines():
            if l[0] == "#":
                ip = int(l.strip().split(" ")[1])
            else:
                program.append(l.strip().split(" "))
                for i,inst in enumerate(program[-1]):
                    if isnum(inst):
                        program[-1][i] = int(inst)
    print("Part 1: {}".format(part1(ip, program, intructions)))
    print("Part 2: {}".format(part2()))



main()