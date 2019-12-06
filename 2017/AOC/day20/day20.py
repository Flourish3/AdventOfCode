dist_dict = {}
pos_dict = {}
vel_dict = {}
acc_dict = {}


index = 0

with open("input.txt") as f:
    for l in f.readlines():
        line = l.split(',')
        for i in range(len(line)):
            line[i] = line[i].rsplit('>')[0]
            tmp = line[i].split('<')
            if len(tmp) > 1:
                line[i] = tmp[1]
        pos_dict[index] = [int(line[0]), int(line[1]), int(line[2])]
        vel_dict[index] = [int(line[3]), int(line[4]), int(line[5])]
        acc_dict[index] = [int(line[6]), int(line[7]), int(line[8])]
        dist_dict[index] = 0
        index += 1

for j in range(1000):
    collision_dict = {}
    to_remove = []
    for i in pos_dict.keys():
        
        dist_dict[i] = abs(pos_dict[i][0]) + abs(pos_dict[i][1]) + abs(pos_dict[i][2])

        vel_dict[i][0] = vel_dict[i][0] + acc_dict[i][0]
        vel_dict[i][1] = vel_dict[i][1] + acc_dict[i][1]
        vel_dict[i][2] = vel_dict[i][2] + acc_dict[i][2]

        pos_dict[i][0] = pos_dict[i][0] + vel_dict[i][0]
        pos_dict[i][1] = pos_dict[i][1] + vel_dict[i][1]
        pos_dict[i][2] = pos_dict[i][2] + vel_dict[i][2]

        pos_tuple = (pos_dict[i][0], pos_dict[i][1], pos_dict[i][2])
        if pos_tuple not in collision_dict:
            collision_dict[pos_tuple] = i
        else:
            to_remove.append(i)
            to_add = collision_dict[pos_tuple]
            if to_add not in to_remove:
                to_remove.append(to_add)

    for r in to_remove:
        pos_dict.pop(r, None)
        vel_dict.pop(r, None)
        acc_dict.pop(r, None)


    print(len(pos_dict))
    print(min(dist_dict, key=dist_dict.get))
