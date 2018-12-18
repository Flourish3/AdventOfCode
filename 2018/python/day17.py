#Advent of Code - Day 17
import re
from collections import defaultdict

def part1(tiles, minY, maxY):
    equilibrium = False
    while not equilibrium:
        for k,w in tiles.items():
            if w == '+' or w == '|':
                x,y = k
                if (x,y+1) not in tiles:
                    tiles[(x,y+1)] = "|"
                elif tiles[(x,y+1)] == "#":
                    i = 0
                    while tiles[(x+i,y)] != "#":
                        tiles[(x+i,y)] = "~"
                        i += 1
                    i = 0
                    while tiles[(x-i,y)] != "#":
                        tiles[(x+i,y)] = "~"
                        i += 1
                elif tiles[(x,y+1)] == "~":
                     i = 0
                    while tiles[(x+i,y)] != "#" and tiles[(x+i,y+1)] == "~":
                        if tiles[(x+i,y)]
                        i += 1






def main():
    tiles = defaultdict(str)
    minY = 0
    maxY = 0

    # Parse to find tiles of clay
    with open("../data/input17.txt") as f:
        for l in f.readlines():
            print(l.strip())
            match = re.findall(r'^(.)=(\d+), (.)=(\d+)..(\d*)$', l.strip())[0]

            if match[0] == "x":
                for y in range(match[3], match[4] + 1):
                    tiles[(match[1], y)] = "#"
                    minY = min(minY, y)
                    maxY = max(maxY, y)
            elif match[0] == "y":
                for x in range(match[3], match[4] + 1):
                    tiles[x, match[1]] = "#"
                minY = min(minY, y)
                maxY = max(maxY, y)
    tiles[(500,0)] = "+"

    print("Part 1: {}".format(part1(tiles, minY, maxY)))


main()
