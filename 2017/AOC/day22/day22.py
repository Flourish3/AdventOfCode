map = {}
x = 12
y = 12
dir = 0
bursts = 10000000
infections = 0


with open("input.txt") as f:
    y_count = 0
    for l in f.readlines():
        x_count = 0
        l = l.strip()
        for c in l:
            if c == '#':
                map[(x_count, y_count)] = 1
            elif c =='.':
                map[(x_count, y_count)] = 0
            x_count += 1
        y_count += 1

for i in range(bursts):
    if map[(x,y)] == 1:
        dir += 1
        if dir > 3:
            dir = 0
        map[(x,y)] = 3
    elif map[(x,y)] == 0:
        dir -= 1
        if dir < 0:
            dir = 3
        map[(x,y)] = 2 #2 is weakened
    elif map[(x,y)] == 2:
        map[(x,y)] = 1
        infections += 1
    elif map[(x,y)] == 3:
        if dir == 0:
            dir = 2
        elif dir == 1:
            dir = 3
        elif dir == 2:
            dir = 0
        elif dir == 3:
            dir = 1
        map[(x,y)] = 0

    
    if dir == 0:
        y -= 1
    elif dir == 1:
        x += 1
    elif dir == 2:
        y += 1
    elif dir == 3:
        x -= 1
    if (x,y) not in map:
        map[(x,y)] = 0
print(infections)

