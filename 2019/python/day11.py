# Advent of code 2019 - day 09
import itertools

lines = open("../data/input11.txt").readline().strip()
lines = lines.split(",")
lines = list(map(lambda x : int(x), lines))

from intcode import *

inp = [int(ins) for ins in open("../data/input11.txt").read().split(",")]



def accessMemory(program, index):
    if index >= len(program):
        print(index, len(program))
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
       # print("#1", intProgram[1])

        if positionanal[2] == 0:
            firstParam = accessMemory(intProgram,accessMemory(intProgram,index+1))
        elif positionanal[2] == 1:
            firstParam = accessMemory(intProgram, index + 1)
        else:
            print("AccessMemory", accessMemory(intProgram, index + 1), relativeIndex, index)
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
        
        #if thirdMemoryPos == 1:
            #print("We have a one", opcode,positionanal[1],secondParam, )
        #print(positionanal, opcode, index, intProgram[index:index+3], firstParam, secondParam)

        if opcode == 0:
            jumpDist = 1

        elif opcode == 1:
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos - len(intProgram) + 1))
            intProgram[thirdMemoryPos] = firstParam + secondParam 
            jumpDist = 4

        elif opcode == 2:
            if thirdMemoryPos > len(intProgram):
                intProgram.extend([0]*(thirdMemoryPos- len(intProgram) + 1))
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
                #print(intProgram[intProgram[index + 1]])
                return (False, intProgram[intProgram[index + 1]], intProgram, index + 2)
            elif positionanal[2] == 1:
                #print(intProgram[index + 1])
                return (False, intProgram[index + 1], intProgram, index + 2)
            else:
                #print(intProgram[intProgram[index + 1]+relativeIndex])
                return (False, intProgram[intProgram[index + 1]+relativeIndex], intProgram, index + 2)
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
    robotX = 0
    robotY = 0
    painted = {}
    heading = 0
    headings = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}

    pc = 0
    linesOut = lines
    finished = False
    while finished == False:
        if (robotX,robotY) not in painted:
            painted[(robotX, robotY)] = 0

        (finished, out,linesOut, pc) = runIntProgram(linesOut,[painted[(robotX, robotY)]], pc)
        painted[(robotX, robotY)] = out
        (finished, out,linesOut, pc) = runIntProgram(linesOut,[], pc)
        if out == 0:
            heading = (heading - 1) % 4
        elif out == 1:
            heading = (heading + 1) % 4
        robotX += headings[heading][0]
        robotY += headings[heading][1]

    return len(painted)

def part2():
    grid = {}
    machine = Machine([j for j in inp])
    robot = (0,0)
    robot_direction = 0
    color = 1
    output_type = 0
    directions = {0: (0,1), 1: (1,0), 2: (0,-1), 3: (-1,0)}
    while True:
        try:
            if output_type == 0:
                machine.run_machine([color])
            else:
                machine.run_machine([])
        except Output as e:
            if output_type == 0:
                grid[robot] = e.output
                output_type = 1
            elif output_type == 1:
                if e.output == 0:
                    robot_direction = (robot_direction - 1) % 4
                if e.output == 1:
                    robot_direction = (robot_direction + 1) % 4
                robot = (robot[0] + directions[robot_direction][0], robot[1] + directions[robot_direction][1])
                if robot in grid:
                    color = grid[robot]
                else:
                    color = 0
                output_type = 0
        except Interrupt:
            break
    
    miny = 0
    minx = 0
    maxy = 0
    maxx = 0
    for cord in grid:
        if cord[0] < minx:
            minx = cord[0]
        if cord[0] > maxx:
            maxx = cord[0]
        if cord[1] < miny:
            miny = cord[1]
        if cord[1] > maxy:
            maxy = cord[1]
    
    painted = [[' ' for _ in range(maxx-minx + 1)] for _ in range(maxy-miny + 1)]
    for cord in grid:
        painted[cord[1]-miny][cord[0]-minx] = '█' if grid[cord] == 1 else ' '

    painted.reverse()
    for row in painted:
        print(''.join(row))
    


#print("Part1: {}".format(part1(lines[:])))
print("Part2: {}".format(part2()))
