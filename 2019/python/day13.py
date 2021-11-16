from intcode import *

inp = [int(ins) for ins in open("../data/input13.txt").read().split(",")]

def part1():
    machine = Machine([j for j in inp])
    grid = {}
    output_type = 0
    x,y = 0,0

    while True:
        try:
            machine.run_machine([])
        except Output as e:
            
            if output_type == 0:
                x = e.output
                output_type = 1
            elif output_type == 1:
                y = e.output
                output_type = 2
            elif output_type == 2:
                if e.output == 0:
                    grid[(x,y)] = " "
                elif e.output == 1:
                    grid[(x,y)] = chr(9609) # Wall
                elif e.output == 2:
                    grid[(x,y)] = "O" # Block
                elif e.output == 3:
                    grid[(x,y)] = "_" #Paddle
                elif e.output == 4:
                    grid[(x,y)] = "o" #Ball
                output_type =0
        except Interrupt:
            break

    return len([v for v in grid.values() if v == "O"])

def part2():
    machine = Machine([j for j in inp])
    grid = {}
    output_type = 0
    x,y = 0,0
    score = 0
    maxX,maxY = 0,0
    while True:
        try:
            machine.run_machine([1])
        except Output as e:
            
            if output_type == 0:
                x = e.output
                maxX = max(maxX, x)
                output_type = 1
            elif output_type == 1:
                y = e.output
                maxY = max(maxY, y)
                output_type = 2
            elif output_type == 2:
                if x == -1 and y == 0:
                    score = e.output
                else:
                    if e.output == 0:
                        grid[(x,y)] = " "
                    elif e.output == 1:
                        grid[(x,y)] = chr(9609) # Wall
                    elif e.output == 2:
                        grid[(x,y)] = "O" # Block
                    elif e.output == 3:
                        grid[(x,y)] = "_" #Paddle
                    elif e.output == 4:
                        grid[(x,y)] = "o" #Ball
                        
                output_type =0
        except Interrupt:
            break
       
        out = "\n".join(["".join([grid[(x,y)] if (x,y) in grid else " " for x in range(maxX)]) for y in range(maxY)])
        print(out)

    return score


print("Part 1: {}".format(part1()))

inp[0] = 2
print("Part 2: {}".format(part2()))