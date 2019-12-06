def knot_hash(key):
    lengths = []
    for c in key:
        lengths.append(ord(c))
    lengths = lengths + [17, 31, 73, 47, 23]
    
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
    return hash_str

def bit_count_hash(hash_n):
    row = []
    
    for c in hash_n:
        c = int(c,16)
        for i in range(4):
            if c & 8:
                row.append(1)
            else:
                row.append(0)
            c <<= 1
    #print("hash: {}, row: {}".format(hash_n, row))
    return row

def find_regions(x, y, matrix):
    if (x < 128) and (y < 128):
        if matrix[x][y] == 1:
            matrix[x][y] = 2
            if x < 127:
                find_regions(x+1,y,matrix)
            if y < 127:
                find_regions(x, y+1, matrix)
            return True
        else:
            #Already found / Nothing here
            return False
    else:
        return False

#input_key = "stpzcrnm"
input_key = "flqrgnkx"
sum_filled = 0
matrix = []
for i in range(128):
    key = input_key + "-" + str(i)
    hash = knot_hash(key)
    matrix.append(bit_count_hash(hash))

print(sum([sum(r) for r in matrix]))

regions = 0

for i in range(128):
    for j in range(128):
        if find_regions(i, j, matrix) == True:
            regions += 1
print(regions)

