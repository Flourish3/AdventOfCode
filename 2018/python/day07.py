#Advent of Code - Day 07


def part1(inputs):
    order = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    moves = 1
    while moves > 0:
        moves = 0
        for i in inputs:
            _, first, _, _, _, _, _, second, _, _ = i.split(" ")

            if order.index(first) > order.index(second):
                order.remove(second)
                ind = order.index(first)+1

                while ind < len(order) and ord(order[ind]) < ord(second):
                    ind += 1
                order.insert(ind, second)
                moves += 1
    return "".join(order)

def part2(inputs, workers = 5):
    prio = []
    for i in inputs:
        _, first, _, _, _, _, _, second, _, _ = i.split(" ")
        prio.append((first,second))

    order = list(part1(inputs))
    done = []
    seconds = 0
    workerList = [[0,0] for i in range(workers)]
    workerList[0][1] = 1

    workPrint = ["Worker {}\t".format(id) for id in range(1,workers+1)]
    print("Second\t{}Done".format("".join(workPrint)))

    while len([left for task, left in workerList if left != 0  ]) > 0:
        for worker in workerList:
            findNewTask = False
            if worker[0] == 0:
                findNewTask = True
            else:
                worker[1] -= 1
                if worker[1] == 0:
                    done.append(worker[0])
                    worker[0] = 0
                    findNewTask = True

            if findNewTask and len(order) > 0:
                available = sorted([o for o in order if len([(first,second) for first,second in prio if o==second and first not in done]) == 0])
                if len(available) > 0:
                    workOrder = available[0]
                    order.remove(workOrder)
                    worker[0] = workOrder
                    worker[1] = 60+ord(workOrder)-64

        workPrint = ["{}{}\t\t".format(task,left) for task, left in workerList]
        for ids,w in enumerate(workerList):
            if w[0] == 0:
                workPrint[ids] = ".\t\t"

        print("{}\t{}\t{}".format(seconds,"".join(workPrint),"".join(done)))
        seconds += 1

    return "".join(done)

def main():
    inputs = [l.strip() for l in open("../data/input07.txt").readlines()]

    print("Part 1: {}".format(part1(inputs)))
    print("Part 2: {}".format(part2(inputs)))

main()
