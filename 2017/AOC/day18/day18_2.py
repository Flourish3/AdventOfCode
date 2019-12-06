import threading

class program (threading.Thread):
    def __init__(self, thread_id, sBuf, rBuf, reg, instuctions):
        threading.Thread.__init__(self)
        self.id = thread_id
        self.sBuf = sBuf
        self.rBuf = rBuf
        self.reg = reg
        self.instructions = instuctions
        self.terminated = False
    def run(self):
        pass

    def decode():

        inst = instuctions[pc]
        pc += 1
        if pc not in instuctions:
            self.terminated = True
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
            self.sBuf.append(reg[inst[1]])
        elif inst[0] == 'rcv':
            if len(r_buf) == 0:
                pc -= 1
            else:
                self.rBuf.pop()

        elif inst[0] == 'jgz':
            if reg[inst[1]] > 0:
                pc -= 1

                pc += int(inst[2])
                if pc in instuctions:
                    self.terminated = False

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
buf1 = []
buf2 = []

t1 = program(1, buf2, buf1)
t2 = program(2, buf1, buf2)




        