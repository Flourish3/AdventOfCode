from typing import Dict, List, Tuple

class Ins():
    def __init__(self, ins, num) -> None:
        self.ins = ins
        self.num = num

def getInput() -> Dict[int, List[str]]:
    with open("08.txt") as f:
        return {i: l.strip().split() for i, l in enumerate(f.readlines())}


def getAccAtFirstRepeated(dic):
    acc = 0
    pc = 0
    seen = set([])
    while pc not in seen:
        seen.add(pc)
        inst = dic[pc]
        if inst[0] == "nop":
            pc += 1
        elif inst[0] == "acc":
            acc += int(inst[1])
            pc += 1
        else:
            pc+= int(inst[1])
    return acc

def runLoop(dic: Dict[int, List[str]], change: int, what: List[str]) -> Tuple[bool, int]:
    acc = 0
    pc = 0
    seen = set([])
    while pc not in seen and pc in dic:
        seen.add(pc)
        inst = []
        if pc == change:
            if what[0] == "nop":
                inst = ["jmp", what[1]]
            else:
                inst = ["nop", what[1]]
        else:
            inst = dic[pc]

        if inst[0] == "nop":
            pc += 1
        elif inst[0] == "acc":
            acc += int(inst[1])
            pc += 1
        else:
            pc+= int(inst[1])
    return pc not in dic, acc

def tryRepair(dic: Dict):
    nopJmp = {k:v for k,v in dic.items() if v[0] == "nop" or v[0] == "jmp"}
    for k,v in nopJmp.items():
        finished, acc = runLoop(dic, k, v)
        if finished:
            return acc
    return 0


def main() -> None:
    dic = getInput()
    print("Part 1: {}".format(getAccAtFirstRepeated(dic)))
    print("Part 2: {}".format(tryRepair(dic)))

main()