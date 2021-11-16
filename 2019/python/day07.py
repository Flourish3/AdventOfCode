# Advent of code 2019 - day 02
import itertools

lines = open("../data/input07.txt").readline().strip()
lines = lines.split(",")
lines = list(map(lambda x : int(x), lines))

def runIntProgram(intProgram, start, pc):
   # intProgram[1] = start
    index = pc
    output = 0

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

        #print(positionanal, opcode, index, intProgram[index])

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
            intProgram[intProgram[index + 1]] = start.pop()
            jumpDist = 2
        elif opcode == 4:
            if positionanal[0] == 0:
                return (False, intProgram[intProgram[index + 1]], intProgram, index + 2)
            else:
                return (False, intProgram[index + 1], intProgram, index + 2)
            
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
    return (True, 0, intProgram, index)

def part1(lines):
    outputs = []
    combinations = [l for l in itertools.permutations([0,1,2,3,4], 5)]
    for c in combinations:
        inp = 0
        oneOut = 0
        for it in c:
            out = runIntProgram(lines[:],[inp, it])
            oneOut = out
            inp = out
        outputs.append(oneOut)
    
    return max(outputs)

def part2(lines):
    outputs = []
    combinations = [l for l in itertools.permutations([5,6,7,8,9], 5)]
    outputs = []
    for c in combinations:
        amplMemory = [[lines[:], phase, 0] for phase in c]
        inp = 0
        lastOutput = 0
        finished = True
    
        # First iterations
        for i in range(5):
            (finished, out,linesOut, pc) = runIntProgram(amplMemory[i][0],[inp, amplMemory[i][1]], amplMemory[i][2])
            amplMemory[i][0] = linesOut
            amplMemory[i][2] = pc
            inp = out
        
        while finished == False:
            for i in range(5):
                (finished, out,linesOut, pc) = runIntProgram(amplMemory[i][0],[inp], amplMemory[i][2])
                amplMemory[i][0] = linesOut
                amplMemory[i][2] = pc
                inp = out
            if finished != True:
                lastOutput = out
        
        outputs.append(lastOutput)

    return max(outputs)
    

#print("Part1: {}".format(part1(lines[:])))
print("Part2: {}".format(part2(lines[:])))
