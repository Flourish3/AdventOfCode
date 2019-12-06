with open("input.txt") as f:
    lengths = []
    for c in f.readline():
        lengths.append(ord(c))
    lengths = lengths + [17, 31, 73, 47, 23]
    print(lengths)
    hash_list = [x for x in range(0,256)]

    current_position = 0
    skip_size = 0

    for i in range(64):
        for length in lengths:
            end_pos = (current_position + length)
            if end_pos > len(hash_list):
                end_pos = end_pos % len(hash_list)
                rev_list = hash_list[current_position:] + hash_list[:end_pos]

                rev_list.reverse()
                end_back = len(hash_list) - current_position
                hash_list[current_position:] = rev_list[:end_back]
                hash_list[:end_pos] = rev_list[end_back:]
            else:
                rev_list = hash_list[current_position:end_pos]
            
                rev_list.reverse()

                hash_list[current_position:end_pos] = rev_list

            
            current_position = (end_pos + skip_size) % len(hash_list)
            skip_size += 1

    dense_hash = []
    for i in range(16):
        h = 0
        for j in range(16):
            h ^= hash_list[i*16 + j]
        if h < 16:
            dense_hash.append('0' + hex(h)[2:])
        else:
            dense_hash.append(hex(h)[2:])
    hash_str = ''.join(dense_hash)
    print(hash_str)