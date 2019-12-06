with open("day1.txt") as f:
    instructions = f.read().strip().split(', ')

x,y = 0,0
dir = 0


visited = []

visited.append((x,y))
foundVisited = False
for i in instructions:
    if i[0] == 'L':
        dir = (dir - 1) % 4

    elif i[0] == 'R':
        dir = (dir + 1) % 4

    steps = int("".join(i[1:]))

    if dir == 0:
        for _ in range(steps):
            y += 1
            if (x,y) in visited:
                foundVisited = True
                break
            visited.append((x,y))
    elif dir == 1:
        for _ in range(steps):
            x += 1
            if (x,y) in visited:
                foundVisited = True
                break
            visited.append((x,y))
    elif dir == 2:
        for _ in range(steps):
            y -= 1
            if (x,y) in visited:
                foundVisited = True
                break
            visited.append((x,y))
    elif dir == 3:
        for _ in range(steps):
            x -= 1
            if (x,y) in visited:
                foundVisited = True
                break
            visited.append((x,y))

    print("x:{} y:{}".format(x,y))
    if foundVisited:
        break



print(str(abs(x) + abs(y)))