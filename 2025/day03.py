def find_max_jolt(bank: list[int], digits: int = 12) -> list[int]:
    if digits == 0:
        return []

    check_bank = bank[:len(bank)-digits + 1]
    m = max(check_bank)

    return [m, *find_max_jolt(bank[check_bank.index(m)+1:] ,digits-1)]

def potens(num_list: list[int]) -> int:
    return sum([i*10**(len(num_list)-idx-1) for idx,i in enumerate(num_list)])

with open("text.txt") as file:
    lines = [list(map(lambda c: int(c), list(line.strip()))) for line in file.readlines()]
    print(sum([potens(find_max_jolt(line,2)) for line in lines ]))
    print(sum([potens(find_max_jolt(line)) for line in lines]))
