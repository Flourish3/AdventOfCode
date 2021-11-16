from functools import reduce


def runSlope(mapp, width, right, down):
    x, y = 0, 0
    treeCount = 0
    while (x, y) in mapp:
        if(mapp[(x, y)]) == "#":
            treeCount += 1
        x = (x + right) % width
        y += down

    return treeCount


def getSlopeMap():
    with open("03.txt") as f:
        lines = f.readlines()
        width = len(lines[0].strip())
        return width, {(x, y): mark for y, line in enumerate(lines) for x, mark in enumerate(list(line.strip()))}


def main():
    width, slopeMap = getSlopeMap()

    print("Part 1: {}".format(runSlope(slopeMap, width, 3, 1)))

    combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    p2 = reduce(lambda a, b: a*b, list(map(lambda combo: runSlope(slopeMap,
                                                                  width, combo[0], combo[1]), combinations)))
    print("Part 2: {}".format(p2))


if __name__ == "__main__":
    main()
