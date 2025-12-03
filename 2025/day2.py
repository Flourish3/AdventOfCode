def repeated_twice(id):
    ids = list(str(id))
    if len(ids) % 2 != 0:
        return False
    return "".join(ids[0 : len(ids) // 2]) == "".join(ids[len(ids) // 2 :])


def id_has_repeated_pattern(id):
    ids = list(str(id))
    # if len(ids) == 2:
    #     return ids[0] == ids[1]
    for div in range(1, len(ids)):
        if len(ids) % div != 0:
            continue
        chunks = ["".join(ids[i : i + div]) for i in range(0, len(ids), div)]
        if len(set(chunks)) == 1:
            return True
    return False


with open("test.txt") as f:
    ids = []
    for r in f.read().split(","):
        ends = r.split("-")
        ids.extend(range(int(ends[0]), int(ends[1]) + 1))

    print(sum(filter(lambda x: repeated_twice(x), ids)))
    print(sum(filter(lambda x: id_has_repeated_pattern(x), ids)))
