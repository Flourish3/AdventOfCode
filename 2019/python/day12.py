# Advent of Code - Day 12
import re
from itertools import permutations

lines = [l.strip() for l in open("../data/input12.txt").readlines()]

class Moon():

    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]
        
    def totalEnergy(self):
        return sum(list(map(lambda x: abs(x), self.pos))) * sum(list(map(lambda x: abs(x), self.vel)))

    def updateVeloicty(self, other, index):
        if self.pos[index] < other.pos[index]:
            self.vel[index] += 1
        elif self.pos[index] > other.pos[index]:
            self.vel[index] -= 1
    
    def updatePosition(self, index):
        self.pos[index] += self.vel[index]

    def __repr__(self):
        return "{}".format(self.pos)
    
    def hash(self):
        return "{}{}".format("".join(list(map(lambda x: str(x),self.pos))), "".join(list(map(lambda x: str(x),self.vel))))

pat = re.compile('^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$')
moon = [Moon(list(map(lambda x: int(x),re.findall(pat, l)[0]))) for l in lines]


iterations = 1000
pairs = [l for l in permutations(moon, 2)]
for it in range(iterations):
    for p in pairs:
        for i in [0,1,2]:
            p[0].updateVeloicty(p[1], i)
    
    for m in moon:
        for i in [0,1,2]:
            m.updatePosition(i)


dimIteration = []
for i in [0,1,2]:
    seen = set()
    found = False
    index = 0
    while found== False:
        moonsHash = "".join([m.hash() for m in moon])
        if moonsHash in seen:
            found = True
            dimIteration.append(index)
        else:
            seen.add(moonsHash)

        for p in pairs:
            p[0].updateVeloicty(p[1], i)
        
        for m in moon:
            m.updatePosition(i)
        index += 1

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)

print("Total enery: {}".format(sum(list(map(lambda p: p.totalEnergy(), moon)))))
print("Number of iterations: {}".format(lcm(dimIteration[0], lcm(dimIteration[1], dimIteration[2]))))
