from typing import Dict, List, Set, Tuple
from functools import reduce

def getInput() -> Tuple[List[Set[str]], List[Set[str]]]:
    with open("21.txt") as f:
        ingredients, allergens = [], []
        for l in f.readlines():
            i, a = l.strip().split(" (contains ")
            ingredients.append(set(i.split(" ")))
            allergens.append(set(a[:-1].split(", ")))
    
    return ingredients, allergens

def getIngredientAllergenMap(allergens: List[Set[str]], ingredients: List[Set[str]]) -> Dict[str, str]:
    found = {}
    uniqAllergens = set(reduce(lambda a,b: a | b, allergens, set()))
    while len(found) < len(uniqAllergens):
        for al in uniqAllergens:
            suspectSeq = reduce(lambda sum,c: sum & c,
                list(map(lambda x: x[1],
                filter(lambda x: al in allergens[x[0]],
                enumerate(ingredients))))) - set(found.keys())
            if len(suspectSeq) == 1:
                found[suspectSeq.pop()] = al
    return found

def main():
    ingredients, allergens = getInput()
    allergenMap = getIngredientAllergenMap(allergens, ingredients)

    print("Part 1: {}".format(reduce(lambda a,b: a + len(b), list(map(lambda x: x - allergenMap.keys(), ingredients)), 0)))    
    print("Part 2: {}".format(",".join(list(map(lambda x: x[0], sorted(list(allergenMap.items()), key = lambda x: x[1]))))))

if __name__ == "__main__":
    main()