# Advent of code 2019 - day 09
import itertools

lines = open("../data/input09.txt").readline().strip()
lines = lines.split(",")
lines = list(map(lambda x : int(x), lines))

def accessMemory(program, index):
    if index >= len(program):
        program.extend([0]*(index-len(program)+1))
    return program[index]

def runIntProgram(intProgram, start, pc):
    index = pc
    output = 0
    relativeIndex = 0
    while intProgram[index] != 99:
        opcode = intProgram[index] % 100
        positionanal = [0,0,0]
        pos = (intProgram[index] - opcode)//100
        positionanal[2] = pos % 10
        positionanal[1] = (pos // 10) % 10 
        positionanal[0] = (pos//100) % 10 


        if positionanal[2] == 0:
            firstParam = accessMemory(intProgram,accessMemory(intProgram,index+1))
        elif positionanal[2] == 1:
            firstParam = accessMemory(intProgram, index + 1)
        else:
            firstParam = accessMemory(intProgram,accessMemory(intProgram, index + 1) + relativeIndex)
        
        if positionanal[1] == 0:
            secondParam = accessMemory(intProgram,accessMemory(intProgram,index+2))
        elif positionanal[1] == 1:
            secondParam = accessMemory(intProgram, index + 2)
        else:
            secondParam = accessMemory(intProgram,accessMemory(intProgram, index + 2) + relativeIndex)

        if positionanal[0] == 0:
            thirdMemoryPos = accessMemory(intProgram, index + 3)
        elif positionanal[0] == 2:
            thirdMemoryPos = accessMemory(intProgram, index + 3) + relativeIndex
        

        #print(positionanal, opcode, index, intProgram[index:index+3], firstParam, secondParam)

        if opcode == 0:
            jumpDist = 1

        elif opcode == 1:
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos))
            intProgram[thirdMemoryPos] = firstParam + secondParam 
            jumpDist = 4

        elif opcode == 2:
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos))
            intProgram[thirdMemoryPos] = firstParam * secondParam
            jumpDist = 4

        elif opcode == 3:
            if positionanal[2] == 0:
                intProgram[intProgram[index + 1]] = start.pop()
            elif positionanal[2] == 2:
                intProgram[intProgram[index + 1] + relativeIndex] = start.pop()
            jumpDist = 2

        elif opcode == 4:
            if positionanal[2] == 0:
                print(intProgram[intProgram[index + 1]])
                #return (False, intProgram[intProgram[index + 1]], intProgram, index + 2)
            elif positionanal[2] == 1:
                print(intProgram[index + 1])
                #return (False, intProgram[index + 1], intProgram, index + 2)
            else:
                print(intProgram[intProgram[index + 1]+relativeIndex])
            jumpDist = 2
        elif opcode == 5: #jump if not zero
            if firstParam != 0:
                index = secondParam
                if index > len(intProgram):
                    intProgram.extend([0]*(secondParam-index))
                jumpDist = 0
            else:
                jumpDist = 3

        elif opcode == 6: # Jump if zero
            if firstParam == 0:
                index = secondParam
                if index > len(intProgram):
                    intProgram.extend([0]*(secondParam-index))
                jumpDist = 0
            else:
                jumpDist = 3

        elif opcode == 7: # Less than    
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos))
            if firstParam < secondParam:
                intProgram[thirdMemoryPos] = 1
            else:
                intProgram[thirdMemoryPos] = 0
            jumpDist = 4

        elif opcode == 8: # equals   
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos))
            if firstParam == secondParam:
                intProgram[thirdMemoryPos] = 1
            else:
                intProgram[thirdMemoryPos] = 0
            jumpDist = 4
        elif opcode == 9: # Modify relative
            relativeIndex += firstParam
            jumpDist = 2
        index += jumpDist
    return (True, 0, intProgram, index)

def part1(lines):
    (finished, out,linesOut, pc) = runIntProgram(lines[:],[1], 0)
    return out

def part2(lines):
    (finished, out,linesOut, pc) = runIntProgram(lines[:],[2], 0)
    return out

print("Part1: {}".format(part1(lines[:])))
print("Part2: {}".format(part2(lines[:])))
