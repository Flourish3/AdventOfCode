# Advent of code - Day 20

from collections import defaultdict

dirs = {
    "N" : (0,1),
    "E" : (1,0),
    "S" : (0,-1),
    "W" : (-1,0)
}

def main():
    # Read input
    line = open("../data/input20.txt").readline().strip()
    positions = []
    x, y = 5000,5000
    prevX, prevY = x,y
    distances = defaultdict(int)

    for c in line[1:-1]:
        if c == "(":
            positions.append((x,y))
        elif c == "|":
            x,y = positions[-1]
        elif c == ")":
            x,y = positions.pop()
        else:
            dx,dy = dirs[c]
            x += dx
            y += dy

        if distances[(x, y)] != 0:
            distances[(x, y)] = min(distances[(x, y)], distances[(prevX, prevY)]+1)
        else:
            distances[(x, y)] = distances[(prevX, prevY)]+1

        prevX, prevY = x, y

    print("Part 1: {}".format(max(distances.values())))
    print("Part 2: {}".format(len([x for x in distances.values() if x >= 1000])))

main()