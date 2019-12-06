input_file = open( "input.txt" )
input_list = list( input_file.read() )

sum = 0

if int(input_list[0]) == int(input_list[-1]):
    sum += int(input_list[0])

for i in range( 0, len( input_list ) - 1 ):
    if input_list[i] == input_list[i+1]:
        sum += int(input_list[i])

print(sum)


