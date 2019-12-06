with open("input.txt") as f:
    score = 0
    depth = 0
    char_garbage = 0
    ignore_next = False
    is_garbage = False
    for line in f:
        for c in line:
            if not ignore_next:
                if c == '<' and not is_garbage:
                    is_garbage = True
                elif c == '>':
                    is_garbage = False 
                elif c == '!':
                    ignore_next = True
                elif c == '{' and not is_garbage:
                    depth += 1
                elif c == '}' and not is_garbage:
                    score += depth
                    depth -= 1
                elif is_garbage:
                    char_garbage += 1
            else:
                ignore_next = False
    print(score)
    print(char_garbage)
