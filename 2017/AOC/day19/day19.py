map = []
with open("input.txt") as f:
    index = 0
    for l in f.readlines():
        map.append([])
        for c in l:
            if c != '\n':
                map[index].append(c)
        index += 1

maxX = len(map[0])
maxY = len(map)
y = 0
x = map[y].index('|')
dir = 2

s_list = []

done = False

steps = 0

while not done:
    
    if map[y][x] == '+':
        #new direction
        if dir == 0 or dir == 2:
            if x > 0:
                if map[y][x-1] != ' ':
                    dir = 3
                    x -= 1
                else:
                    dir = 1
                    x += 1
            else:
                dir = 1
                x += 1
        else:
            if y > 0:
                if map[y-1][x] != ' ':
                    dir = 0
                    y -= 1
                else:
                    dir = 2
                    y += 1
            else:
                dir = 2
                y += 1

    else:
        if map[y][x] != '-' and map[y][x] != '|':
            s_list.append(map[y][x])
            print("x: {}, y:{}, map: {}".format(x,y, map[y][x]))
        if x < maxX and x >= 0 and y < maxY and y >= 0:
            if dir == 0:
                y -= 1
            elif dir == 1:
                x += 1
            elif dir == 2:
                y += 1
            elif dir == 3:
                x -= 1
        else:
            done = True
        if map[y][x] == ' ':
            done = True
    steps += 1   
        
print(''.join(s_list))            
print(steps)
    
