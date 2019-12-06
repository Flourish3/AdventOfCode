# Advent of code - Day 25
from collections import Counter

def partOfConst(p1,p2):
    return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2]) + abs(p1[3]-p2[3])) <=3

def part1(points):
    constellationTracker = {}
    nbrConst = 0

    for p in points:
        constellationTracker[p] = nbrConst
        nbrConst += 1

    changes = 1
    while changes > 0:
        changes = 0
        for k,v in constellationTracker.items():

            for i in range(len(points)):
                if partOfConst(k, points[i]) and constellationTracker[points[i]] != v:
                    for key,value in constellationTracker.items():
                        if value == constellationTracker[points[i]]:
                            constellationTracker[key] = v
                            changes += 1

    return len(Counter(constellationTracker.values()))


def main():
    points = []
    lines = open("../data/input25.txt").readlines()
    for l in lines:
        a,b,c,d = list(map(int,l.strip().split(",")))
        points.append((a,b,c,d))

    print("Part 1: {}".format(part1(points)))



main()