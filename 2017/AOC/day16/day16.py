from collections import deque

with open("input.txt") as f:
    for line in f.readlines():
        l = line.split(',')
        program_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
        dance_line = deque(program_list)
        for i in range(1000000000):
            for move in l:
                if(move[0] == 's'):
                    dance_line.rotate(int(move[1:]))
                elif(move[0] == 'x'):
                    li = move[1:].split('/')
                    index1 = int(li[0])
                    index2 = int(li[1])

                    program1 = dance_line[index1]
                    program2 = dance_line[index2]
                    dance_line[index1] = program2
                    dance_line[index2] = program1

                elif(move[0] == 'p'):
                    li = move[1:].split('/')
                    index1 = dance_line.index(li[0])
                    index2 = dance_line.index(li[1])

                    program1 = dance_line[index1]
                    program2 = dance_line[index2]
                    dance_line[index1] = program2
                    dance_line[index2] = program1
    print(''.join(dance_line))

               