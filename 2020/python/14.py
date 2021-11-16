from typing import List
import re

memPat = re.compile("^mem\[(\d+)\] = (\d+)$")


def set_bit(value: int, bit: int) -> int:
    return value | (1 << bit)


def clear_bit(value:int, bit:int) -> int:
    return value & ~(1 << bit)


def applyMask(mask: str, num: int) -> int:
    for i, x in enumerate(list(mask)):
        if x == "1":
            num = set_bit(num, 35-i)
        elif x == "0":
            num = clear_bit(num, 35-i)

    return num


def getSumOfValues(instList: List[str]) -> int:
    mask = ""
    mem = {}

    for ins in instList:
        if ins.startswith("mask = "):
            mask = ins.split(" = ")[-1]
        else:
            print(mask)
            index, num = re.match(memPat, ins).groups()
            mem[index] = applyMask(mask, int(num))

    return sum(mem.values())


def main():
    instList = [l.strip() for l in open("14.txt").readlines()]
    print(f"Part 1: {getSumOfValues(instList)}")


if __name__ == "__main__":
    main()
