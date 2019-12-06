class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.holding = []
    def __repr__(self):
        return self.name + " " + str(self.weight)

def setup_tree(node, dict):
    if len(dict[node].holding) == 0:
        return
    else:
        for n in dict[node].holding:
            setup_tree(n.name,dict)
            n.weight = dict[n.name].weight

def find_weigth(node,dict):
    if len(dict[node].holding) == 0:
        return dict[node].weight
    else:
        weights = []
        for i in range(0,len(dict[node].holding)):
            weights.append(find_weigth(dict[node].holding[i].name,dict))
        weights.sort()
        if weights[0] != weights[-1]:
            print(weights)
            print(dict[node].holding[2].weight)
        return sum(weights) + dict[node].weight

with open("input.txt") as f:
    dict_start = {}
    dict_leafs = {}
    dict_prog = {}

    for f in f.readlines():
        program = f.split(' ')
        if len(program) > 2:
            program[-1] = program[-1].rsplit('\n')[0]
        for i in range(0,len(program)):
            program[i] = program[i].rsplit(',')[0]
        program[1] = program[1].split('(')[1]
        program[1] = int(program[1].split(')')[0])
        

        dict_start[program[0]] = 1
        if len(program) > 2:
            for i in range(3, len(program)):
                dict_leafs[program[i]] = 1
        
        new_p = Program(program[0], program[1])
        if len(program) > 2:
            for i in range(3,len(program)):
                new_p.holding.append(Program(program[i],0))
        
        dict_prog[program[0]] = new_p

        #print(program)
    #print(len(dict_prog))
    
    root_name = ''

    for k in dict_start.keys():
        if k not in dict_leafs:
            root_name = k
    
    setup_tree(root_name, dict_prog)
    find_weigth(root_name, dict_prog)
