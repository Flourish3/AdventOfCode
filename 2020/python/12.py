from typing import List

directionMap = {0: [0,1], 1: [1,0], 2: [0, -1], 3: [-1,0]}
weatherMap = {"N": [0,1], "E": [1,0], "S": [0, -1], "W": [-1,0]}
rotateMap = {"R": [1, -1], "L": [-1, 1]}

def refinedManhattan(instructions: List[str]) -> int:
    xw,yw, xs, ys = 10, 1, 0,0
    for i in instructions:
        dir = i[0]
        dist = int(i[1:])
        if dir in weatherMap:
            xw, yw =  xw + weatherMap[dir][0]*dist, yw + weatherMap[dir][1]*dist
        elif dir in rotateMap:
            for _ in range(dist // 90):
                oldX = xw
                xw = (rotateMap[dir][0]*(yw-ys)) + xs
                yw = (rotateMap[dir][1]*(oldX-xs)) + ys
        elif dir == "F":
            moveX, moveY = xw - xs, yw-ys
            xs,ys = xs + moveX*dist, ys + moveY*dist
            xw,yw = xw + moveX*dist, yw + moveY*dist

    return abs(xs) + abs(ys)


def getManhattanDistanceAfterInstructions(instructions: List[str]) -> int:
    x,y,direction = 0,0,1
    for i in instructions:
        dir = i[0]
        dist = int(i[1:])

        if dir in weatherMap:
            x, y =  x + weatherMap[dir][0]*dist, y + weatherMap[dir][1]*dist
        elif dir in rotateMap:
            direction = (direction + rotateMap[dir][0]*dist // 90) % 4
        elif dir == "F":
            x,y = x + directionMap[direction][0]*dist, y + directionMap[direction][1]*dist

    return abs(x) + abs(y)

def main():
    inputSequence = [l.strip() for l in open("12.txt").readlines()]
    print(f"Part 1: {getManhattanDistanceAfterInstructions(inputSequence)}")
    print(f"Part 2: {refinedManhattan(inputSequence)}")

if __name__ == "__main__":
    main()