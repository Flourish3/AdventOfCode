# Advent of code - day19

from intcode import *
import math

inp = [int(ins) for ins in open("../data/input19.txt").read().split(",")]

machine = Machine([j for j in inp])
grid = {}
x,y = 0,0
startX, startY = 0,0
limitP1 = 50
limitP2 = 1000

while x < limitP1:
    foundOut = False
    while y < limitP2:
        try:
            machine = Machine([j for j in inp])
            machine.run_machine([y,x])
        except Output as e:
            if e.output == 0:
                grid[(x,y)] = (0,0,0)
                if foundOut:
                    break
            elif e.output == 1:
                if x == 0:
                    xSum = 0
                else:
                    if (x-1,y) in grid:
                        xSum = grid[(x-1,y)][1] + 1
                    else:
                        xSum = 1
                if y == 0:
                    ySum = 0
                else:
                    if (x,y-1) in grid:
                        ySum = grid[(x,y-1)][2] + 1
                    else:
                        ySum = 1
                grid[(x,y)] = (1,xSum, ySum)
                if foundOut == False:
                    startY = max(y,0) 
                    foundOut = True
            
        except Interrupt:
            print("break")
            
        y += 1
       
    x += 1
    y = startY


def part1():
            
    for y in range(limitP1):
        print("".join(["#" if (x,y) in grid and grid[(x,y)][0] == 1 else "." for x in range(limitP1)]))
    return len([ grid[(x,y)] for x in range(limitP1) for y in range(limitP1) if (x,y) in grid and grid[(x,y)][0] == 1])

def part2():
    machine = Machine([j for j in inp])
    grid = {}
    x,y = 950,1000
    startX, startY = 0,0
    limitP2 = 1000
    foundShip = False
    xShip, yShip = 0,0
    while not foundShip:
        foundOut = False
        while not foundShip:
            try:
                machine = Machine([j for j in inp])
                machine.run_machine([x,y])
            except Output as e:
                if e.output == 0:
                    grid[(x,y)] = (0,0,0)
                    if foundOut:
                        # Found the bottom 1 step up
                        if y > 100:
                            yPass = False
                            xPass = False
                            try:
                                machine = Machine([j for j in inp])
                                machine.run_machine([x+99, y-100])
                            except Output as e:
                                if e.output == 1:
                                    xPass = True
                                    foundShip = True
                                    xShip = x
                                    yShip = y-100

                        startY = max(0,y-1)
                        break
                elif e.output == 1:
                  
                    if foundOut == False:
                        #startY = max(y,0) 
                        foundOut = True
                
            except Interrupt:
                print("break")
                
            y += 1
        
        x += 1
        y = startY

    return (xShip*10000)+yShip


def scan(x, y):
    try:
        machine = Machine([j for j in inp])
        machine.run_machine([x,y])
    except Output as e:
        return e.output


def get_slopes():
    x = 0
    y = 10000
    while not scan(x, y):
        x += 1
    x2 = x
    while scan(x, y):
        x += 1
    x1 = x
    return y / x1, y / x2


def get_ratios():
    x = 0
    y = 10000
    while not scan(x, y):
        x += 1
    x1 = x
    while scan(x, y):
        x += 1
    x2 = x
    return y / x2, y / x1

def cheat():

    m1, m2 = get_ratios()
    x2 = ((m1 * 99) + 99) / (m2 - m1)
    y1 = (m2 * x2) - 99
    print(x2, y1)
    print(round(x2), round(y1))

#print("Part 1: {}".format(part1()))

print("Part 2: {}".format(part2()))

#print("Cheat: {}", cheat())