# Advent of code - Day 22

def erosion(x,y,erotions,depth):

    if erotions[x][y] is not None:
        return erotions[x][y]

    gi = 0
    if y == 0 and x != 0:
        gi = x * 16807
    elif x == 0 and y != 0:
        gi = y * 48271
    else:
        gi = erosion(x,y-1,erotions,depth) * erosion(x-1,y,erotions,depth)

    erotions[x][y] = (gi+depth) % 20183

    return erotions[x][y]

def part1(depth, target,erotions):
    return sum(erosion(x,y,erotions,depth) % 3 for x in range(target[0]+1) for y in range(target[1]+1))


def main():
    lines = open("../data/input22.txt").readlines()
    depth, target = int(lines[0].strip().split(": ")[1]), list(map(int,lines[1].strip().split(": ")[1].split(",")))

    erotions = [[None for _ in range(target[1]+10)] for _ in range(target[0]+10)]
    erotions[0][0] = 0
    erotions[target[0]][target[1]] = 0

    print("Part 1: {}".format(part1(depth, target, erotions)))

main()