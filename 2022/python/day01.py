def get_elf_food_list():
    with open("2022/data/day01.txt") as f:
        elf_food_str_list = f.read().split("\n\n")
        return list(map(lambda elf: [int(s) for s in elf.split("\n")], elf_food_str_list))
        
def max_food():
    print(max(map(lambda x: sum(x), get_elf_food_list())))

def top_three_food():
    print(sum(sorted(list(map(lambda x: sum(x), get_elf_food_list())))[-3:]))


if __name__ == "__main__":
    max_food( )
    top_three_food()