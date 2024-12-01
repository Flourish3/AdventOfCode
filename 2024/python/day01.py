with open("data/day01.txt") as f:
    l1, l2 = [], []
    for l in f.readlines():
        t1, t2 = l.strip().split("   ")
        l1.append(int(t1))
        l2.append(int(t2))

    print(sum(map(lambda x: abs(x[0]-x[1]), list(zip(sorted(l1), sorted(l2))))))

    print(sum(map(lambda x: x * len([item for item in l2 if item == x]), l1)))