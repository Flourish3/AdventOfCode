#Advent of Code - Day 06
from collections import defaultdict, Counter

inputs = [l.strip() for l in open("../data/input06.txt").readlines()]

coords = set()
max_x = max_y = 0
for i in inputs:
    x,y = map(int, i.split(", "))
    coords.add((x,y))
    max_x = max(max_x, x)
    max_y = max(max_y, y)

cordIdPoint = {coord_id : point for coord_id,point in enumerate(coords, start = 1)}

# Part 1
areas = defaultdict(int)
infiniteIds = set()

for x in range(max_x+1):
    for y in range(max_y+1):
        min_dists = sorted([(abs(c-x)+abs(r-y),cord_id) for cord_id, (c,r) in cordIdPoint.items()])

        if len(min_dists) == 1  or min_dists[0][0] != min_dists[1][0]:
            cord = min_dists[0][1]
            areas[min_dists[0][1]] += 1

            #If we are at the border, the closet point will be an infinite point
            if x == 0 or y == 0 or x == max_x or y == max_y:
                infiniteIds.add(cord)

maxArea = max([area for coord, area in areas.items() if coord not in infiniteIds])

#Part 2
closeArea = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        closeArea += int(sum([abs(x-c)+abs(y-r) for (c,r) in cordIdPoint.values()]) < 10000)


print("Part 1: {}".format(maxArea))
print("part 2: {}".format(closeArea))