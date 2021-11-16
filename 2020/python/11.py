from typing import Dict, Tuple


def getInput():
    with open("11.txt") as f:
        seatArea = {(x,y): c for y,line in enumerate(f.readlines()) for x,c in enumerate(list(line.strip())) }
        maxX = max(list(map(lambda x: x[0], seatArea.keys())))
        maxY = max(list(map(lambda x: x[1], seatArea.keys())))
        return seatArea, maxX, maxY

def findNextSeat(seatingArea, x, y, xs, ys):
    xf, yf = x,y
    while (xf+xs, yf+ys) in seatingArea and seatingArea[(xf+xs, yf+ys)] == ".":
        xf, yf = xf+xs, yf+ys
    if (xf+xs, yf+ys) not in seatingArea:
        return "."
    else:
        return seatingArea[(xf+xs, yf+ys)]

def occupiedAroundRefined(seatingArea, x, y):
    occupied = 0
    for xs in [-1, 0, 1]:
        for ys in [-1, 0, 1]:
            if (xs, ys) != (0,0) and findNextSeat(seatingArea, x, y, xs, ys) == "#":
                occupied += 1
    #print(occupied)
    return occupied

def runIterationRefined(seatingArea):
    changed = 0
    oldSeat = seatingArea.copy()
    lines = []
    #for y in range(10):
     #   lines.append("".join([seatingArea[(x,y)] for x in range(10)]))
    #print("\n".join(lines))
    #print("\n")

    for x,y in seatingArea.keys():
        occupied = occupiedAroundRefined(oldSeat, x, y)
        if oldSeat[(x,y)] == "L" and occupied == 0: 
            seatingArea[(x,y)] = "#"
            changed += 1
        elif oldSeat[(x,y)] == "#" and occupied >= 5:
            seatingArea[(x,y)] = "L"
            changed += 1
    return changed

def getSeatsRefined(seatingArea):
    while runIterationRefined(seatingArea) > 0:
        pass
    return countSitting(seatingArea)


def occupiedAround(seatingArea, x, y):
    occupied = 0
    for xs in [-1, 0, 1]:
        for ys in [-1, 0, 1]:
            if (x+xs, y+ys) in seatingArea and (x+xs,y+ys) != (x,y) and seatingArea[(x+xs, y+ys)] == "#":
                occupied += 1
    return occupied

def runIteration(seatingArea, maxX, maxY):
    changed = 0
    oldSeat = seatingArea.copy()

    for x,y in seatingArea.keys():
        occupied = occupiedAround(oldSeat, x, y)
        if oldSeat[(x,y)] == "L" and occupied == 0: 
            seatingArea[(x,y)] = "#"
            changed += 1
        elif oldSeat[(x,y)] == "#" and occupied >= 4:
            seatingArea[(x,y)] = "L"
            changed += 1
    return changed

def countSitting(seatingArea: Dict[Tuple[int,int], str]) -> int:
    return len([c for c in seatingArea.values() if c == "#"])

def getSeatsAtStabilized(seatingArea, maxX, maxY):
    while runIteration(seatingArea, maxX, maxY) > 0:
        pass
    return countSitting(seatingArea)

def main():
    seatingArea, maxX, maxY = getInput()
    print(f"Part 1: {getSeatsAtStabilized(seatingArea.copy(), maxX, maxY)}")
    print(f"Part 2: {getSeatsRefined(seatingArea.copy())}")

if __name__ == "__main__":
    main()