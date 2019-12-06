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
    while registers[ip] < len(program):
        currentInstruction = program[registers[ip]]
        registers = instructions[currentInstruction[0]](currentInstruction, registers)
        registers[ip] += 1
        #print(registers, currentInstruction)

    return registers

def part1(ip, program, instructions):
    registers = execute([0,0,0,0,0,0], ip, program, instructions)

    return registers[0]

def part2(ip, program, instructions):

    ans = 0
    sqrt_n = int(n**.5)

    return registers[0]


def main():
    ip = 0
    program = []

    intructions = {}
    instructionNames = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    instructionFunctions= [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    for name,instr in zip(instructionNames, instructionFunctions):
        intructions[name] = instr

    with open("../data/input19.txt") as f:
        for l in f.readlines():
            if l[0] == "#":
                ip = int(l.strip().split(" ")[1])
            else:
                program.append(l.strip().split(" "))
                for i,inst in enumerate(program[-1]):
                    if isnum(inst):
                        program[-1][i] = int(inst)

    print("Part 1: {}".format(part1(ip, program, intructions)))
    a,b = int(program[21][2]), int(program[23][2])
    n1 = 836 + 22*a + b
    n = n1 + 10550400
    sqrt_n = int(n**.5)
    print(sum(d+n//d for d in range(1,sqrt_n + 1) if n%d == 0)-(sqrt_n * (sqrt_n**2==n)))



main()