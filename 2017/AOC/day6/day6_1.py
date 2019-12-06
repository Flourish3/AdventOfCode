compositions = {}
value = 1
counter = 0

def noUnique(list):
    tmp_list = [str(x) for x in list]
    tmp_list = ''.join(tmp_list)
    if tmp_list in compositions:

        return (False, compositions[tmp_list]) 
    else:
        compositions[tmp_list] = counter
        return (True, 0)



with open("input.txt") as f:
    list = [int(x) for x in f.readlines()[0].split('\t')]
    
    
    (loop, final) = noUnique(list)
    while loop:
        jumps = max(list)
        index = list.index(jumps)
        
        list[index] = 0
        while jumps > 0:
            if index + 1 < len(list):
                index += 1
            else:
                index = 0
            
            list[index] += 1
            jumps -= 1
        
        counter += 1
        (loop, final) = noUnique(list)
    print(final)
    print(len(compositions))

    print(counter - final)
