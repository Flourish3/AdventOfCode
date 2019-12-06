# Advent of code 2019 - day 02

lines = open("../data/input02.txt").readline().strip()
lines = lines.split(",")
lines = list(map(lambda x : int(x), lines))

def runIntProgram(intProgram, start, second):
    intProgram[1] = start
    intProgram[2] = second 
    index = 0

    while intProgram[index] != 99:
        if intProgram[index] == 1:
            intProgram[intProgram[index + 3]] = intProgram[intProgram[index + 1]] + intProgram[intProgram[index + 2]]
        elif intProgram[index] == 2:
            intProgram[intProgram[index + 3]] = intProgram[intProgram[index + 1]] * intProgram[intProgram[index + 2]]
        index += 4
    return intProgram[0]

def part1(lines):
    return runIntProgram(lines,12,2)

def part2(lines, vaueToFind):
    for i in range(100):
        for j in range(100):
            if runIntProgram(lines[:], i, j) == vaueToFind:
                return 100 * i+ j

print("Part1: {}".format(part1(lines[:])))
print("Part2: {}".format(part2(lines[:], 19690720)))