from typing import List, Tuple
from functools import reduce


def get_string_halves(input: str) -> Tuple[str, str]:
    stripped_input = input.strip()
    index = len(stripped_input) // 2

    return (stripped_input[0 : index], stripped_input[index:])


def read_input(in_str: str) -> List[Tuple[str,str]]:
    with open(in_str) as f:
        return [ get_string_halves(l) for l in f.readlines()]

def get_score(char: str) -> int:
    
    if ord(char) >= 97:
        #print(ord(char)-96)
        return ord(char)-96
    else:
        #print(ord(char)-64 + 26)
        return ord(char) - 64 + 26

def get_score_for_incorrect(input: List[Tuple[str, str]]) -> int:
    return sum([get_score(set(first).intersection(set(second)).pop()) for first, second in input])


def chunk_3(list_str: List[str]):
    for i in range(0, len(list_str), 3):
        yield list_str[i:i+3]

def get_common(sub_list: List[str]) -> str:
    return reduce(lambda x,y: x.intersection(y), list(map(set, sub_list)), set).pop()

def get_score_for_badge(input: List[Tuple[str,str]]):
    return sum(map(get_score, list(map(get_common, list(chunk_3(list(map(lambda x: x[0] + x[1], input))))))))


if __name__ == "__main__":
    input = read_input("2022/data/day03.txt")
    print(get_score_for_incorrect(input))
    print(get_score_for_badge(input))
