import sys
import math
from functools import cache

@cache
def num_stones(number: int, iterations: int) -> int:
    if iterations == 0:
        return 1

    if number == 0:
        return num_stones(1, iterations-1)

    num_digit = math.floor(math.log10(number) + 1)
    if  num_digit % 2 == 0:
        return sum([num_stones(number//(10**(num_digit/2)),iterations - 1), num_stones(number % 10**(num_digit//2), iterations -1)])

    return num_stones(number*2024, iterations -1)

with open(sys.argv[1]) as f:
    stones = list(map(lambda x: int(x), f.read().strip().split()))
    print("Part 1:", sum(map(lambda s: num_stones(s, 25), stones)))
    print("Part 2:", sum(map(lambda s: num_stones(s, 75), stones)))
