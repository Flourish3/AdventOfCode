# Advent of code - Day 24

def printGrid(g, n):
    print("Depth: {}".format(n))
    print("\n".join(["".join([g[(n, x,y)] for x in range(5)]) for y in range(5)]))
    print("\n")

def calculateBiodiversiry(g):
    return sum([b * 2**i for i,b in enumerate([1 if g[(0,x,y)]=="#" else 0 for y in range(5) for x in range(5)])])

def coordsSurroundedRec(n, x, y):
    if x == 2 and y == 2:
        return []

    coords = []
    if y == 0:
        coords.extend([(n-1,2,1), (n,x,1)])
    elif y == 4:
        coords.extend([(n-1,2,3), (n,x,3)])
    elif y == 1 and x == 2:
        coords.append((n, 2, 0))
        for i in range(5):
            coords.append((n+1, i, 0))
    elif y == 3 and x == 2:
        coords.append((n, 2, 4))
        for i in range(5):
            coords.append((n+1, i, 4))
    else:
        coords.extend([(n,x,y-1), (n,x,y+1)])
    
    if x == 0:
        coords.extend([(n-1,1,2), (n,1,y)])
    elif x == 4:
        coords.extend([(n-1,3,2), (n,3,y)])
    elif x == 1 and y == 2:
        coords.append((n, 0, 2))
        for i in range(5):
            coords.append((n+1, 0, i))
    elif x == 3 and y == 2:
        coords.append((n, 4, 2))
        for i in range(5):
            coords.append((n+1, 4, i))
    else:
        coords.extend([(n,x-1,y), (n,x+1,y)])
    
    return coords


def getSurrounded(g, n, x, y, p2):
    if p2:
        coords = coordsSurroundedRec(n, x, y)
    else:
        coords = [(n,x,y-1), (n,x-1,y), (n,x+1, y), (n,x,y+1)]

    return list(map(lambda coord: g[coord] if coord in g else ".", coords)).count("#")

def getAlive(g, n, x, y, p2):
    surroundCount = getSurrounded(g, n, x, y, p2)
    
    if (n,x,y) not in g:
        g[(n,x,y)] =  "."

    if g[(n,x,y)] == "#" and surroundCount != 1:
        return "."
    elif g[(n,x,y)] == "." and (surroundCount == 1 or surroundCount == 2):
        return "#"
    else:
        return g[(n,x,y)]

def calculateNewGrid(g):
    return {(0,x,y): getAlive(g, 0, x, y, False) for x in range(5) for y in range(5) }

def calculateNewGridRec(g):
    levelKeys = set(map(lambda key: key[0], g.keys()))
    minN, maxN = min(levelKeys)-1, max(levelKeys)+2
    return {(n,x,y): getAlive(g, n, x, y, True) for n in range(minN, maxN) for x in range(5) for y in range(5)}

oriGrid = {(0,x,y): c for y,line in enumerate([l.strip() for l in open("../data/input24.txt").readlines()]) for x,c in enumerate(list(line)) }

seenBios = set()
grid = oriGrid.copy()
bioDiv = calculateBiodiversiry(grid)

while bioDiv not in seenBios:
    seenBios.add(bioDiv)
    grid = calculateNewGrid(grid)
    bioDiv = calculateBiodiversiry(grid)

minutes = 200
grid = oriGrid.copy()
for _ in range(minutes):
    grid = calculateNewGridRec(grid)

for i in range(-6, 7):
    printGrid(grid, i)

print("Part 1 - First biodiv to appear twice: {}".format(bioDiv))
print("Part 2 - Number of bugs: {}".format([v for v in grid.values()].count("#")))
