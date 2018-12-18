#Advent of Code - Day 18
from collections import Counter

def findAdjacent(x, y, forest, size):
    trees = lumbers = 0
    for i in [-1,0,1]:
        for k in [-1,0,1]:
            if x+i >= 0 and x+i < size and y+k >= 0 and y+k < size:
                if i == 0 and k == 0:
                    pass
                else:
                    if forest[x+i][y+k] == "|":
                        trees += 1
                    elif forest[x+i][y+k] == "#":
                        lumbers += 1
    return trees, lumbers


def part1(forest,size):
    minutes = 10

    print("Initial")
    for i in range(size):
            print("".join(forest[:][i]))

    for m in range(minutes):
        newForest = [[0]*size for x in range(size)]
        for x in range(size):
            for y in range(size):
                trees, lumberyards = findAdjacent(x, y, forest, size)
                if forest[x][y] == ".":
                    if trees >= 3:
                        newForest[x][y] = "|"
                    else:
                        newForest[x][y] = "."
                elif forest[x][y] == "|":
                    if lumberyards >= 3:
                        newForest[x][y] = "#"
                    else:
                        newForest[x][y] = "|"
                elif forest[x][y] == "#":
                    if trees >= 1 and lumberyards >= 1:
                        newForest[x][y] = "#"
                    else:
                        newForest[x][y] = "."

        forest = newForest
        print(m)
        for i in range(size):
            print("".join(forest[:][i]))

    trees = lumber = 0
    counter = [Counter(r) for r in forest]
    for c in counter:
        trees += c['|']
        lumber += c["#"]

    return trees * lumber



def main():
    size = 50
    forest = [[0]*size for x in range(size)]

    with open("../data/input18.txt") as f:
        x = 0
        for l in f.readlines():
            for i,c in enumerate(l.strip()):
                forest[x][i] = c
            x+= 1

    print("Part 1: {}".format(part1(forest,size)))


main()
