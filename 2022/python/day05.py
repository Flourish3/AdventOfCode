""" 
[S]                 [T] [Q]        
[L]             [B] [M] [P]     [T]
[F]     [S]     [Z] [N] [S]     [R]
[Z] [R] [N]     [R] [D] [F]     [V]
[D] [Z] [H] [J] [W] [G] [W]     [G]
[B] [M] [C] [F] [H] [Z] [N] [R] [L]
[R] [B] [L] [C] [G] [J] [L] [Z] [C]
[H] [T] [Z] [S] [P] [V] [G] [M] [M]
 1   2   3   4   5   6   7   8   9  """


def get_moves():
    with open("2022/data/day05.txt") as f:
        return [list(filter(lambda x: x.isnumeric() == True, line.strip().split(" "))) for line in f.readlines()]


if __name__ == "__main__":
    moves = list(map(lambda x: list(map(lambda y: int(y), x)), get_moves()))
    stack = [
        ["H", "R", "B", "D", "Z", "F", "L", "S"],
        ["T", "B", "M", "Z", "R"],
        ["Z", "L", "C", "H", "N", "S"],
        ["S", "C", "F", "J"],
        ["P", "G", "H", "E", "R", "Z", "B"],
        ["V", "J", "Z", "G", "D", "N", "M", "T"],
        ["G","L","N","W","F","S","P","Q"],
        ["M","Z","R"],
        ["M","C","L","G","V","R","T"]
    ]

    #for move in moves:
    #    print(move)
    #    for _ in range(move[0]):
    #        to_move = stack[move[1]-1].pop()
    #        stack[move[2]-1].append(to_move)

    for move in moves:
        to_move = stack[move[1]-1][-move[0]:]
        [ stack[move[1]-1].pop() for _ in range(move[0])]
        print(move, stack[move[1]-1], to_move)
        stack[move[2]-1].extend(to_move)

    print("".join([v[-1] for v in stack]))
        

