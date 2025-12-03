from itertools import accumulate
import math


def get_all_clicks(start, steps) -> list[int]:
    sign = int(math.copysign(1, steps))
    return list(
        map(
            lambda x: x % 100,
            range(start + sign, start + steps + sign, sign),
        )
    )


with open("test.txt") as f:
    n = [int(c) for c in f.readlines()]
    res = list(accumulate([50, *n], lambda a, b: (a + b) % 100))
    print(res)
    print(res.count(0))

    r = [50]
    for num in n:
        print(r[-1])
        r.extend(get_all_clicks(r[-1], num))
    print(r)
    print(r.count(0))
