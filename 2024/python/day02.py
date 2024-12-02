import sys

def is_levels_safe(numbers) -> bool:
    res = list(zip(numbers[:-1], numbers[1:]))
    diff = list(map(lambda x: x[0]-x[1], res))
    ab = list(map(lambda x: abs(x), diff))

    return max(ab) <=3 and \
           min(ab) >= 1 and \
           (all(map(lambda x: x < 0, diff)) or all(map(lambda x: x > 0, diff)))

with open(sys.argv[1]) as f:
    tot = 0
    for l in f.readlines():
        numbers = list(map(lambda x: int(x), l.strip().split(" ")))

        if is_levels_safe(numbers):
            tot += 1
        else:
            for idx, d in enumerate(numbers):
                if is_levels_safe([n for idy, n in enumerate(numbers) if idx != idy ]):
                    tot += 1
                    break

    print(tot)