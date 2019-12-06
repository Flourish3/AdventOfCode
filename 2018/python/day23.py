# Advent of code - Day 23

import re

class Bot():
    def __init__(self, x, y, z, strength):
        self.x = x
        self.y = y
        self.z = z
        self.strength = strength

    def dist(self, other):
        return abs(self.x-other.x) + abs(self.y - other.y) + abs(self.z - other.z)

def part1(bots):
    maxSig = 0
    maxBot = None
    for b1 in bots:
        if b1.strength > maxSig:
            maxSig = b1.strength
            maxBot = b1


    botCount = 0
    for b2 in bots:
        if maxBot.dist(b2) <= maxBot.strength:
            botCount += 1

    return botCount

def main():
    bots = []
    botsInput = open("../data/input23.txt").readlines()
    for bot in botsInput:
        botParse = re.findall(r"pos=<([-]?\d*),([-]?\d*),([-]?\d*)>, r=(\d*)", bot)
        x,y,z,r = list(map(int,botParse[0]))
        bots.append(Bot(x,y,z,r))
    print("Part 1: {}".format(part1(bots)))

main()