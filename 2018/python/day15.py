#Advent of Code - Day 15
from collections import defaultdict

class Unit():
    def __init__(self,race, x, y):
        self.x = x
        self.y = y
        self.race = race
        self.hitPoints = 200

    def __eq__(self, other):
        return self.race == other.race

    def __lt__(self, other):
        status = False
        if self.y < other.y:
            status = True
        elif self.y == other.y and self.x < other.x:
            status = True

        return status

    def adjacent(self, other):
        if self.x == other.x and abs(self.y-other.y) == 1:
            return True
        elif self.y == other.y and abs(self.x-other.x) == 1:
            return True
        else:
            return False

    def distance(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

def round(cave, combatants):
    for c in combatants:
        # Attack first
        opponent = min([op for op in combatants if c.adjacent(op)], key=lambda x : x.hitPoints, default=None)
        if opponent != None:
            opponent.hitPoints -= 3

            if opponent.hitPoints <= 0:
                combatants.remove(opponent)
            continue

        # Move
        distances =







def part1(cave, combatants):

    roundCount = 0
    while len(set([c.race for c in combatants])) == 2:
        if round(cave, combatants):
            combatants.sort()
            roundCount += 1

    return roundCount * sum([c.hitPoints for c in combatants])

def main():
    cave = defaultdict(str)
    combatants = []

    y = 0
    for l in open("../data/input15.txt").readlines():
        for x,c in enumerate(l.strip()):
            if c == "G" or c == "E":
                combatants.append(Unit(c,x,y))
                cave[(x,y)] = "."
            else:
                cave[(x,y)] = c
        y += 1

    print("Part1: {}".format(part1(cave, combatants)))

main()
