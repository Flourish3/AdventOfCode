#Advent of Code - Day 12
from collections import defaultdict

def nextGen(plants, rules):
    maxN = max(plants)
    minN = min(plants)


    nextG = set()
    for i in range(minN-2, maxN + 3):
        pattern = ["#" for k in [-2,-1,0,1,2] if ]



def solve(rules, plants, offset, generations):

    for g in range(1,generations+1):
        newPlants = ['.']*len(plants)
        for p in range(2, len(plants)-2):
            newPlants[p] = rules["".join(plants[p-2:p+3])]
        plants = newPlants

    gensum = 0
    for i,p in enumerate(plants):
        if p == '#':
            gensum += i-offset

    return gensum

def main():
    inFile = open("../data/input12.txt")
    plants = []

    rules = defaultdict(str)
    plants = set([i for i,c in enumerate(inFile.readline().strip().split(": ")[1]) if c == '#'])

    for l in inFile.readlines():
       if l != "\n":
            rule = l.strip().split(" => ")
            rules[rule[0]] = rule[1]
    inFile.close()

    print("Part 1: {}".format(solve(rules, plants, offset, 20)))

    #After visual investigation: diff = 75 after 2000 iterations

    diff = 75
    generations = 50000000000
    ans = solve(rules, plants, offset, 2000)+(generations-2000)*diff

    print("Part 2: {}".format(ans))

main()
