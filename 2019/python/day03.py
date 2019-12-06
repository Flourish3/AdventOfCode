import shapely
from shapely.geometry import LineString, Point

lines = [l.strip() for l in open("../data/input03.txt").readlines()]
  

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def new_intersect(line1, line2):
    line1 = LineString([line1[0], line1[1]])
    line2 = LineString([line2[0], line2[1]])

    int_pt = line1.intersection(line2)
    point_of_intersection = int_pt.x, int_pt.y
   
    return point_of_intersection


def getLines(wire):
    currentCoords = [0,0]
    wireLines = []
    currentSteps = 0
    for w in wire.split(","):
        steps = int(w[1:])
        currentSteps += steps
        if w[0] == "R":
            newCoords = [currentCoords[0] + steps, currentCoords[1]] 
        elif w[0] == "L":
            newCoords = [currentCoords[0] - steps, currentCoords[1]]
        elif w[0] == "U":
            newCoords = [currentCoords[0], currentCoords[1] + steps]
        elif w[0] == "D":
            newCoords = [currentCoords[0], currentCoords[1] - steps]

        wireLines.append(((currentCoords, newCoords),currentSteps) )
        currentCoords = newCoords
    return wireLines


def part1(intersections):
    return sorted(list(map(lambda x: abs(x[0][0]) + abs(x[0][1]), intersections)))[0]

def part2(lines):
    return sorted( intersections,key=lambda x: x[1])[0]

def subFromLine(line, point):
    diffLine = (point, line[1])
    return abs(diffLine[0][0]-diffLine[1][0]) + abs(diffLine[0][1] - diffLine[1][1])

linesFirstWire = getLines(lines[0])
linesSecondWire = getLines(lines[1])
#linesFirstWire = getLines("R75,D30,R83,U83,L12,D49,R71,U7,L72")
#linesSecondWire = getLines("U62,R66,U55,R34,D71,R55,D58,R83")
intersections = []
for fi in linesFirstWire:
    for se in linesSecondWire:
        try:
            intersect = new_intersect(fi[0],se[0])
            #print(fi, se, intersect)
            if intersect[0] != 0 and intersect[1] != 0:
                steps = fi[1] + se[1] - subFromLine(fi[0], intersect) - subFromLine(se[0], intersect)
                intersections.append((intersect, steps))
        except Exception:
            pass
print("intersections", intersections)
#print("sorted, dist",sorted(list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))))

print("Part 1: {}".format(part1(intersections)))
#print("Part 1: {}".format(part1("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")))
#print("Part 1: {}".format(part1("R8,U5,L5,D3", "U7,R6,D4,L4")))
print("Part 2: {}".format(part2(intersections)))
