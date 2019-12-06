inFile = open("input.txt")

def change_reg(op, reg, num):
    if op == 'inc':
        register[reg] += num
    else:
        register[reg] -= num

register = {}
max_reg = 0

for l in inFile.readlines():
    
    inst = l.split(' ')
    inst[2] = int(inst[2])
    inst[-1] = int(inst[-1].rsplit("\n")[0])

    if inst[4] not in register:
        register[inst[4]] = 0
        
    if inst[0] not in register:
        register[inst[0]] = 0

    if inst[5]== '==':
        if register[inst[4]] == inst[6]:
            change_reg(inst[1], inst[0], inst[2])
    elif inst[5]== '!=':
        if register[inst[4]] != inst[6]:
            change_reg(inst[1], inst[0], inst[2])
    elif inst[5]== '<=':
        if register[inst[4]] <= inst[6]:
            change_reg(inst[1], inst[0], inst[2])
    elif inst[5]== '>=':
        if register[inst[4]] >= inst[6]:
            change_reg(inst[1], inst[0], inst[2])
    elif inst[5]== '<':
        if register[inst[4]] < inst[6]:
            change_reg(inst[1], inst[0], inst[2])
    elif inst[5]== '>':
        if register[inst[4]] > inst[6]:
            change_reg(inst[1], inst[0], inst[2])

    for v in register.values():
        if v>max_reg:
            max_reg = v   




print(max_reg)