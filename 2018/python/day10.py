#Advent of Code - Day 10

def determineTime(inputs):
    minI = 0
    minBound = 2000000
    for i in range(20000):
        maxX = max([x+dx*i for x,y,dx,dy in inputs])
        minX = min([x+dx*i for x,y,dx,dy in inputs])
        maxY = max([y+dy*i for x,y,dx,dy in inputs])
        minY = min([y+dy*i for x,y,dx,dy in inputs])

        if minBound > (maxX-minX + maxY-minY):
            minI = i
            minBound = maxX-minX + maxY-minY
    return minI

def printMessage(time, inputs):

    mapp = [[' ']*200 for i in range(200)]
    for x,y,dx,dy in inputs:
        mapp[x+time*dx][y+time*dy] = '*'
    for m in mapp:
        print(''.join(m))

def main():
    posVel = []
    maxX = 0
    maxY = 0
    inputs = open("../data/input10.txt").readlines()
    for i in inputs:
        i = i.strip()
        i = i.split("<")
        x, y = i[1].split(">")[0].split(", ")
        dx,dy = i[2].split(">")[0].split(", ")

        posVel.append(list(map(int,[x,y,dx,dy])))
    time = determineTime(posVel)
    print("Part 1:")
    printMessage(time, posVel)
    print("Part 2: {}".format(time))

main()