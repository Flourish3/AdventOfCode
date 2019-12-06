def findNbrPipes(pipe, inDict, visitDict):
    if pipe in visitDict:
        return
    else:     
        visitDict[pipe] = 1
        for p in inDict[pipe]:
            if p not in visitDict:
                findNbrPipes(p, inDict, visitDict)
            
        return    

with open("input.txt") as f:
    pipe_dict = {}
    connections = 0
    for l in f.readlines():
        inLine = l.strip().split(' ')
        pipe_dict[int(inLine[0])] = []
        for i in range(2,len(inLine)):
            inPipe = int(inLine[i].rsplit(',')[0])
            pipe_dict[int(inLine[0])].append(inPipe)
            if(inPipe == 0):
                connections += 1
    
    master_visited = {}
    groups = 0
    for p in pipe_dict:
        if p not in master_visited:
            visited = {}
            visited[p] = 1
            for pipe in pipe_dict[p]:
                findNbrPipes(pipe, pipe_dict, visited)
            master_visited.update(visited)
            groups += 1
    print(groups)