def match_low_16_bits(a,b):
    if (a & 65535) == (b & 65535):
        return True
    return False

a_start = 873
b_start = 583

#a_start = 65
#b_start = 8921

factor_a = 16807
factor_b = 48271

div_rem = 2147483647
nbr_pairs = 5000000

nbr_match = 0
done = False

a_buf = []
b_buf = []

a_gen = (a_start * factor_a) % div_rem
b_gen = (b_start * factor_b) % div_rem
if a_gen % 4 == 0:
    a_buf.append(a_gen)
if b_gen % 8 == 0:
    b_buf.append(b_gen)

while not done:
    if len(a_buf) < nbr_pairs:
        a_gen = (a_gen*factor_a) % div_rem 
        if a_gen % 4 == 0:
            a_buf.append(a_gen)
    if len(b_buf) < nbr_pairs:
        b_gen = (b_gen*factor_b) % div_rem
        if b_gen % 8 == 0:
            b_buf.append(b_gen)
    if (len(a_buf) >= nbr_pairs) and (len(b_buf) >= nbr_pairs):
        done = True
print(len(a_buf))
print(len(b_buf))
for a,b in zip(a_buf, b_buf):
    if match_low_16_bits(a, b):
        nbr_match += 1

print(nbr_match)