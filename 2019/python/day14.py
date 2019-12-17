# Advent of Code - Day 14

import re
import math
import collections

lines = [l.strip() for l in open("../data/input14.txt").readlines()]

groupFind = re.compile(r"((\d+) (\w+))")

class Material():
    def __init__(self, name, quantity, ingredients):
        self.name = name
        self.created = int(quantity)
        self.ingrediends = list(map(lambda ingredient: (
            int(ingredient[0]), ingredient[1]), ingredients))

    def __repr__(self):
        return "Name: {}, creates {} from {}".format(self.name, self.created, ", ".join(list(map(lambda x: x[1], self.ingrediends))))

materialList = []
for l in lines:
    split = l.split("=>")
    result = re.findall(groupFind, split[1])[0]
    ingredients = [p[1:] for p in re.findall(groupFind, split[0])]

    materialList.append(Material(result[2], result[1], ingredients))

matDict = {m.name: m for m in materialList}

def getIngredForMaterial(name, needed, leftOvers):
    material = matDict[name]
    takenFromLeftOver = 0
    while name  in leftOvers:
        takenFromLeftOver += 1
        leftOvers.remove(name)
    iterationsNeeded = math.ceil((needed-takenFromLeftOver)/material.created)
    leftOvers.extend([name]*(iterationsNeeded*material.created-((needed-takenFromLeftOver))))

    ingredientsNeeded = list(map(lambda ingredient: (ingredient[0] * iterationsNeeded, ingredient[1]), material.ingrediends))

    oresNeededList = 0
    for need, ingredient in ingredientsNeeded:

        if ingredient == "ORE":
            oresNeededList += need
        else:
            oresUsed, leftOvers = getIngredForMaterial(ingredient, need, leftOvers)
            oresNeededList += oresUsed


    return oresNeededList, leftOvers


leftOvers = []
oreToFuel, leftOvers = getIngredForMaterial("FUEL", 1, leftOvers)
totalOre = 1000000000000

minFuel = math.floor(totalOre/oreToFuel)
maxFuel = 2*math.floor(totalOre/oreToFuel)

while maxFuel - minFuel > 1:
    midOre, left = getIngredForMaterial("FUEL", math.floor((maxFuel+minFuel)/2), [])

    if midOre < totalOre:
        minFuel = math.floor((maxFuel+minFuel)/2)
    else:
        maxFuel = math.floor((maxFuel+minFuel)/2)

print("Part 1: {} ".format(oreToFuel))
print("Part 2: {}".format(minFuel))
