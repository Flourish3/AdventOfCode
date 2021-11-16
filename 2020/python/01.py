import itertools
from functools import reduce

def getExpenses(combinations: int) -> int:
    return list(map(lambda x: reduce(lambda a,b: a*b, x, 1), filter(lambda x: sum(x) == 2020,itertools.combinations(expenses, combinations))))[0]

with open("01.txt") as f:
    expenses = [int(x) for x in f.readlines()]
    print("Part 1: {}".format(getExpenses(2)))
    print("Part 2: {}".format(getExpenses(3)))
