# Advent of code 2019 - day 02

lines = open("../data/input05.txt").readline().strip()
lines = lines.split(",")
lines = list(map(lambda x : int(x), lines))

def runIntProgram(intProgram, start):
   # intProgram[1] = start
    index = 0

    while intProgram[index] != 99:
        opcode = intProgram[index] % 100
        positionanal = [0,0,0]
        pos = (intProgram[index] - opcode)//100
       # print("BEfore assign", pos, pos%10, pos % 10 == 1)
        if pos % 10 == 1:
            positionanal[2] = 1
        if (pos // 10) % 10 == 1:
            positionanal[1] = 1
        if (pos//100) % 10 == 1:
            positionanal[0] = 1

        print(positionanal, opcode, index, intProgram[index])

        if opcode == 0:
            jumpDist = 1
        elif opcode == 1:
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]


            intProgram[intProgram[index + 3]] = firstParam + secondParam 
            jumpDist = 4
        elif opcode == 2:
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]

            intProgram[intProgram[index + 3]] = firstParam * secondParam
            jumpDist = 4
        elif opcode == 3:
            intProgram[intProgram[index + 1]] = start
            jumpDist = 2
        elif opcode == 4:
            if positionanal[0] == 0:
                print(intProgram[intProgram[index + 1]])
            else:
                print(intProgram[index + 1])
            jumpDist = 2
        elif opcode == 5:
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]
            
            if firstParam != 0:
                index = secondParam
                jumpDist = 0
            else:
                jumpDist = 3

        elif opcode == 6:
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]
            
            if firstParam == 0:
                index = secondParam
                jumpDist = 0
            else:
                jumpDist = 3
        elif opcode == 7: # Less than
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]
            
            if firstParam < secondParam:
                intProgram[intProgram[index + 3]] = 1
            else:
                intProgram[intProgram[index + 3]] = 0
            jumpDist = 4
        elif opcode == 8: # equals
            if positionanal[2] == 0:
                firstParam = intProgram[intProgram[index + 1]]
            else:
                firstParam = intProgram[index + 1]
            
            if positionanal[1] == 0:
                secondParam = intProgram[intProgram[index + 2]]
            else:
                secondParam = intProgram[index + 2]
            
            if firstParam == secondParam:
                intProgram[intProgram[index + 3]] = 1
            else:
                intProgram[intProgram[index + 3]] = 0
            jumpDist = 4
        index += jumpDist
    return intProgram[0]

def part1(lines):
    return runIntProgram(lines,1)

def part2(lines):
    return runIntProgram(lines,5)

print("Part1: {}".format(part1(lines[:])))
print("Part2: {}".format(part2(lines[:])))
