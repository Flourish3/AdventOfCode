reg_keys = list('abcdefghijklmnopqrstuvwxyz')

registers_0 = {}
registers_1 = {}
for key in reg_keys:
    registers_0[key] = 0
    registers_1[key] = 0

instuctions = {}


with open("input.txt") as f:
    index = 0
    for l in f.readlines():
        line = l.strip().split(' ')
        instuctions[index] = line
        index += 1

pc_0 = 0
pc_1 = 0

buf_0 = []
buf_1 = []

program_id = 0

def decode(reg, s_buf, r_buf, pc):
    terminated = False
    waiting = False
    inst = instuctions[pc]
    pc += 1
    if pc not in instuctions:
        terminated = True
    if inst[0] == 'set':
        if inst[2].isalpha():
            reg[inst[1]] = reg[inst[2]]
        else:
            reg[inst[1]] = int(inst[2])
    elif inst[0] == 'add':
        reg[inst[1]] += int(inst[2]) 
    elif inst[0] == 'mul':
        reg[inst[1]] *= int(inst[2])
    elif inst[0] == 'mod':
        if inst[2].isalpha():
            reg[inst[1]] = reg[inst[1]] % reg[inst[2]]
        else:
            reg[inst[1]] = reg[inst[1]] % int(inst[2])
    elif inst[0] == 'snd':
        s_buf.append(reg[inst[1]])
    elif inst[0] == 'rcv':
        if len(r_buf) == 0:
            pc -= 1
            waiting = True
        else:
            waiting = False
            r_buf.pop()

    elif inst[0] == 'jgz':
        if reg[inst[1]] > 0:
            pc -= 1

            pc += int(inst[2])
            if pc in instuctions:
                terminated = False
    return (terminated, waiting)

end = False
t0 = False
t1 = False

w0 = False
w1 = False
send_times = 0

while not end:
    if program_id == 0:
        t0,w0 = decode(registers_0, buf_1, buf_0, pc_0)
        program_id = 1
    elif program_id == 1:
        buf_len = len(buf_0)
        t1,w1 = decode(registers_1, buf_0, buf_1, pc_1)
        if len(buf_0) > buf_len:
            send_times += 1
        program_id = 0
    if (t0 == True and t1 == True) or (w0 == True and w1 == True):
        end = True
print(send_times)

