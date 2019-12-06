#Advent of Code - Day 13
from collections import defaultdict

class Cart():
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.turnDir = 0
        self.crashed = False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        status = False
        if self.y < other.y:
            status = True
        elif self.y == other.y and self.x < other.x:
            status = True

        return status


def crashed(carts):
    for i in range(len(carts)):
        for k in range(i+1,len(carts)):
            if carts[i] == carts[k]:

                return True
    return False

def tick(carts, tracks, first = True):
    print([(c.x,c.y) for c in carts])
    crash1 = 0
    crash2 = 0
    crashedFound = False
    for car in carts:
        if car.crashed:
            pass
        print(car.x,car.y,car.dir)
        if car.dir == 0:
            nextTrack = tracks[(car.x,car.y-1)]
            if nextTrack == '/':
                car.dir = 1
            elif nextTrack == '\\':
                car.dir = 3
            elif nextTrack == '+':
                if car.turnDir == 0:
                    car.dir = 3
                elif car.turnDir == 2:
                    car.dir = 1
                car.turnDir = (car.turnDir + 1) % 3
            car.y -= 1

        elif car.dir == 1:
            nextTrack = tracks[(car.x+1,car.y)]
            if nextTrack == '/':
                car.dir = 0
            elif nextTrack == '\\':
                car.dir = 2
            elif nextTrack == '+':
                if car.turnDir == 0:
                    car.dir = 0
                elif car.turnDir == 2:
                    car.dir = 2
                car.turnDir = (car.turnDir + 1) % 3
            car.x += 1
        elif car.dir == 2:
            nextTrack = tracks[(car.x,car.y+1)]
            if nextTrack == '/':
                car.dir = 3
            elif nextTrack == '\\':
                car.dir = 1
            elif nextTrack == '+':
                if car.turnDir == 0:
                    car.dir = 1
                elif car.turnDir == 2:
                    car.dir = 3
                car.turnDir = (car.turnDir + 1) % 3
            car.y += 1

        elif car.dir == 3:
            nextTrack = tracks[(car.x-1,car.y)]
            if nextTrack == '/':
                car.dir = 2
            elif nextTrack == '\\':
                car.dir = 0
            elif nextTrack == '+':
                if car.turnDir == 0:
                    car.dir = 2
                elif car.turnDir == 2:
                    car.dir = 0
                car.turnDir = (car.turnDir + 1) % 3
            car.x -= 1
 #       print([(c.x,c.y) for c in carts])
        if crashed(carts):
            found = False
            for i in range(len(carts)):
                for k in range(i+1,len(carts)):
                    if carts[i] == carts[k]:
                        carts[i].crashed = True
                        carts[k].crashed = True
                        crash1 = i
                        crash2 = k
                        crashedFound = True
                        found = True
                        break
                if found:
                    break
    if crashedFound:
        del carts[crash1]
        del carts[crash2]


#                print("After:",len(carts), [(c.x,c.y) for c in carts])

def part1(carts, tracks):
    while not crashed(carts):
        tick(carts, tracks)
        carts.sort()

    for i in range(len(carts)):
        for k in range(i+1,len(carts)):
            if carts[i] == carts[k]:
                return (carts[i].x, carts[i].y)

def part2(carts, tracks):
    while len(carts) > 1:
        tick(carts, tracks, False)
        carts.sort()
        print([(c.x,c.y) for c in carts])

    return (carts[0].x,carts[0].y)


def main():
    carts = []
    tracks = defaultdict(str)

    y = 0
    for l in open("../data/input13.txt").readlines():
        for x,c in enumerate(l):
            if c == "<" or c == ">":
                direction = 3 if c=='<' else 1
                carts.append(Cart(x,y,direction))
                tracks[(x,y)] = '-'
            elif c == "^" or c == "v":
                direction = 0 if c=='^' else 2
                carts.append(Cart(x,y,direction))
                tracks[(x,y)] = '|'
            elif c != ' ' and  c !='\n':
                tracks[(x,y)] = c
        y += 1

   # print("Part 1: {}".format(part1(carts, tracks)))
    print("Part 2: {}".format(part2(carts, tracks)))

main()
