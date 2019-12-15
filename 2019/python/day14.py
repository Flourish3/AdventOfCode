# Advent of Code - Day 14

import re
import math

lines = [l.strip() for l in open("../data/input14.txt").readlines()]

groupFind = re.compile(r"((\d+) (\w+))")


class Material():

    def __init__(self, name, quantity, ingredients):
        self.name = name
        self.created = int(quantity)
        self.ingrediends = list(map(lambda ingredient: (
            int(ingredient[0]), ingredient[1]), ingredients))
        print(self.ingrediends)

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
    mat = matDict[name]
    iterationsNeeded = math.ceil(needed/mat.created)

    ingredientsNeeded = list(map(lambda ingredient: (ingredient[0] * iterationsNeeded, ingredient[1]), mat.ingrediends))

    oresNeededList = []
    for i in ingredientsNeeded:
        takenFromLeftOver = 0
        while i[1]  in leftOvers:
            takenFromLeftOver += 1
            leftOvers.remove(i[1])

        if i[1] == "ORE":
            leftOvers.extend(["ORE"]*(i[0]-needed))
            oresNeededList.extend(["ORE"]*needed)
        else:
            oresNeededList.append(getIngredForMaterial(i[1], i[0], leftOvers))


    return oresNeededList


leftOvers = []
print("Part 1: {} ".format(getIngredForMaterial("FUEL", 1, leftOvers)))
