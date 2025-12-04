def check_for_roll(all_rolls, row, col) -> bool:
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    count = 0
    max = len(all_rolls)

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < max and 0 <= new_col < max and all_rolls[new_row][new_col] == "@":
            count += 1
    return count < 4


with open("test.txt") as file:
    all_rolls = [list(line.strip()) for line in file.readlines()]
    total_count = 0

    while True:
        to_remove = []
        count = 0
        for x in range(len(all_rolls)):
            for y in range(len(all_rolls)):
                if all_rolls[y][x] == "@" and check_for_roll(all_rolls, y, x):
                    count += 1
                    to_remove.append((x, y))
        total_count += count
        if count == 0:
            break
        while len(to_remove) > 0:
            remove = to_remove.pop()
            all_rolls[remove[1]][remove[0]] = "."

        print(count)
    print(total_count)
