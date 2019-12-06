lines = [l.strip() for l in open("../data/input06.txt").readlines()]


def part1(dic):
    count = 0
    for k in dic.keys():
        while k in dic:
            k = dic[k]
            count += 1
    return count

def findOrbit(dic, orbit, start):
    orbitCounter = 0
    while start != orbit and dic[start] != "COM":
        start = dic[start]
        orbitCounter += 1
    if dic[start] == "COM":
        return (0,False)
    else:
        return (orbitCounter, True)

def part2(dic):
    sanOrbit = dic["SAN"]
    youOrbit = dic["YOU"]
    santaSteps = 0
    foundSanta = False
    while foundSanta == False and sanOrbit != "COM":
        (steps, foundSanta) = findOrbit(dic, sanOrbit, youOrbit)
        if foundSanta:
            return santaSteps + steps
        else:
            sanOrbit = dic[sanOrbit]
            santaSteps += 1


orbitDic = {}
for l in lines:
    [center, orbit] = l.split(")")
    orbitDic[orbit] = center

print("Part1: {}".format(part1(orbitDic)))
print("Part2: {}".format(part2(orbitDic)))
