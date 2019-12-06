input_file = open( "input.txt" )
input_list = list( input_file.read() )

length = len(input_list)
jump = length / 2

def get_next_input(index):
    tmp = int((index + jump) % length )
    return tmp

sum = 0

for i in range( 0, len( input_list ) - 1 ):
    if input_list[i] == input_list[get_next_input(i)]:
        sum += int(input_list[i])

print(sum)