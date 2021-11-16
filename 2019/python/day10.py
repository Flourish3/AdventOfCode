import math
from collections import deque

lines = [l.strip() for l in open("../data/input10.txt").readlines()]
astroids = []
y=0
for l in lines:
    x=0
    for c in l:
        if c == "#":
           astroids.append(([x,y]))
        x+= 1
    y+=1 

def angleBetweenPoints(a, b):
    return math.atan2(b[1]-a[1], b[0]- a[0])

def numberAnglesForPoint(point, restOfPoints):
    return [(angleBetweenPoints(point, p),p) for p in restOfPoints if not (p[0] == point[0] and p[1] == point[1])]

def findUniqueAngles(ast):
    seen = set()
    ret = []
    for a in ast:
        if a[0] not in seen:
            seen.add(a[0])
            ret.append(a) 
    return ret

astroidsAndPoint = [numberAnglesForPoint(p, astroids) for p in astroids]
maxAstroids = max(astroidsAndPoint, key = lambda x: len(findUniqueAngles(x)))
print("Maximum astrois seen: {}".format(len(findUniqueAngles(maxAstroids))))

queue = deque(sorted(findUniqueAngles(maxAstroids), key = lambda x: x[0]))
while queue[0][0] < -math.pi / 2:
    queue.rotate(-1)
twoHundreds = queue[199][1]
print((twoHundreds[0]*100)+twoHundreds[1])
