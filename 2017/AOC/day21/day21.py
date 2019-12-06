#start 
       # .#.
       # ..#
       # ###

def find_ones(s):
    return sum([x.count(1) for x in s])

input_patterns = {}
output_patters = {}
index = 0
with open("input.txt") as f:
    for l in f.readlines():
        line = l.strip().split(" => ")
        inp = line[0].split('/')
        outp = line[1].split('/')
        
        in_pat = []
        for i in inp:
            tmp = []
            for c in i:
                if c == '#':
                    tmp.append(1)
                elif c == '.':
                    tmp.append(0)
            in_pat.append(tmp)
        input_patterns[index] = in_pat

        out_pat = []
        for i in outp:
            tmp = []
            for c in i:
                if c == '#':
                    tmp.append(1)
                elif c == '.':
                    tmp.append(0)
            out_pat.append(tmp)
        output_patters[index] = out_pat

        index += 1

square = [[0,1,0],[0,0,1],[1,1,1]]

size = 3
nbr_ones = find_ones(square)

for i in range(5):
    if size % 2 == 0:
        pass
    elif size % 3 == 0:
        pass        

print(nbr_ones)