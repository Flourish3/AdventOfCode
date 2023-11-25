

from typing import Set, Tuple
from functools import reduce

def get_tree_map():
    with open("2022/data/day08.txt") as f:
        return [[int(s) for s in list(line.strip())] for line in f.readlines()]


def from_the_outside(tree_map):
    visible = set()

    for x in range(len(tree_map)):
        # up - down
        tallest_up_down = 0
        tallest_down_up = 0
        for y in range(len(tree_map)):
            if x == 0 or y == 0:
                visible.add((x,y))
                tallest_up_down = tree_map[y][x]
            else:
                if tree_map[y][x] > tallest_up_down:
                    visible.add((x,y))
                    tallest_up_down = tree_map[y][x]

            reverse_y = len(tree_map) - 1 - y
            if reverse_y == len(tree_map) - 1:
                visible.add((x,reverse_y))
                tallest_down_up = tree_map[reverse_y][x]
            else:
                if tree_map[reverse_y][x] > tallest_down_up:
                    visible.add((x,reverse_y))
                    tallest_down_up = tree_map[reverse_y][x]
    
    for y in range(len(tree_map)):
        # left - right
        tallest_left_right = 0
        tallest_right_left = 0
        for x in range(len(tree_map)):
            if x == 0 or y == 0:
                visible.add((x,y))
                tallest_left_right = tree_map[y][x]
            else:
                if tree_map[y][x] > tallest_left_right:
                    visible.add((x,y))
                    tallest_left_right = tree_map[y][x]

            reverse_x = len(tree_map) - 1 - x
            if reverse_x == len(tree_map)-1:
                visible.add((reverse_x,y))
                tallest_right_left = tree_map[y][reverse_x]

            else:
                if tree_map[y][reverse_x] > tallest_right_left:
                    visible.add((reverse_x,y))
                    tallest_right_left = tree_map[y][reverse_x]
    print(visible)
    print(len(visible))


def view_score(x,y,tree_map):
    view_distance = []

    # Down
    num_tree = 0
    for idx in range(y+1, len(tree_map)):
        if idx < 0 or idx >= len(tree_map):
            pass
        elif tree_map[idx][x] == tree_map[y][x]:
            num_tree += 1
            break
        elif tree_map[idx][x] < tree_map[y][x]:
            num_tree += 1
        else:
            break
    view_distance.append(num_tree)

    # Up
    num_tree = 0
    for idx in range(y-1, -1,-1):
        if idx < 0 or idx >= len(tree_map):
            pass
        elif tree_map[idx][x] == tree_map[y][x]:
            num_tree += 1
            break
        elif tree_map[idx][x] < tree_map[y][x]:
            num_tree += 1
        else:
            break
    view_distance.append(num_tree)
   
   # Right
    num_tree = 0
    for idx in range(x+1, len(tree_map)):
        if idx < 0 or idx >= len(tree_map):
            pass
        elif tree_map[y][idx] >= tree_map[y][x]:
            num_tree += 1
            break
        elif tree_map[y][idx] < tree_map[y][x]:
            num_tree += 1
        else:
            break
    view_distance.append(num_tree)
    
    # Left
    num_tree = 0
    for idx in range(x-1, -1, -1):
        if idx < 0 or idx >= len(tree_map):
            pass
        elif tree_map[y][idx] == tree_map[y][x]:
            num_tree += 1
            break
        elif tree_map[y][idx] < tree_map[y][x]:
            num_tree += 1
        else:
            break
    view_distance.append(num_tree)

    return reduce((lambda x,y: x*y), view_distance)


def get_max_view_score(tree_map):
    return max([view_score(x,y,tree_map) for y in range(len(tree_map)) for x in range(len(tree_map))])

if __name__ == "__main__":
    tree_map = get_tree_map()
    
    from_the_outside(tree_map)
    print(get_max_view_score(tree_map))
