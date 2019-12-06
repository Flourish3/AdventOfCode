def match_low_16_bits(a,b):
    if (a & 65535) == (b & 65535):
        return True
    return False

a_start = 873
b_start = 583

a_start = 65
b_start = 8921

factor_a = 16807
factor_b = 48271

div_rem = 2147483647
nbr_pairs = 5000000

nbr_match = 0
done = False

a_buf = []
b_buf = []

a_pushed = 0
b_pushed = 0

a_gen = (a_start * factor_a) % div_rem
b_gen = (b_start * factor_b) % div_rem
if a_gen % 4 == 0:
    a_buf.append(a_gen)
if b_gen % 8 == 0:
    b_buf.append(b_gen)

while not done:
    if a_pushed < nbr_pairs:
        a_gen = (a_gen*factor_a) % div_rem 
        if a_gen % 4 == 0:
            a_buf.append(a_gen)
            a_pushed += 1
    if b_pushed < nbr_pairs:
        b_gen = (b_gen*factor_b) % div_rem
        if b_gen % 8 == 0:
            b_buf.append(b_gen)
            b_pushed += 1

    if (len(a_buf)>0) and (len(b_buf)>0):
        if (a_pushed == nbr_pairs) and (b_pushed == nbr_pairs):
            done = True
        a = a_buf.pop(0)
        b = b_buf.pop(0)
        if match_low_16_bits(a, b):
            nbr_match += 1

print(nbr_match)


