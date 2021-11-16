# Advent of code - Day 15

from intcode import *

inp = [int(ins) for ins in open("../data/input15.txt").read().split(",")]

hallway = {}
directions = {1: (0,1), 2: (0,-1), 3: (-1,0), 4: (1,0)}

def generateMap():
    machine = Machine([j for j in inp])
    x,y = 0,0
    direction = 1
    foundOxygen = False

    while not foundOxygen:
        try:
            machine.run_machine([direction])
        except Output as e:
            print(e.output, direction)
            if e.output == 0: # Didn't move
                xs, ys = [sum(x) for x in zip((x,y),directions[direction])]
                hallway[(xs, ys)] = "#"
                direction = direction % 4 + 2

            elif e.output == 1: # Moved in direction, no oxygen
                x,y = [sum(x) for x in zip((x,y),directions[direction])]
                hallway[(x,y)] = "."
                
            else: # moved in direction, found oxygen tank
                x,y = [sum(x) for x in zip((x,y),directions[direction])]
                hallway[(x,y)] = "O"
                foundOxygen = True
                print("Done")
          
        except Interrupt:
            print("Breaking")
            break
    xs = [v[0] for v in hallway.keys()]
    ys = [v[1] for v in hallway.keys()]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    for y in range(ymin, ymax + 1):
        out = []
        for x in range(xmin, xmax + 1):
            if (x,y) in hallway:
                out.append(hallway[(x,y)])
            else:
                out.append(" ")
        print("".join(out))

def part1():
    

    return 0

generateMap()
print("Part 1: {}".format(part1()))

#print("Part 2: {}".format(part2()))