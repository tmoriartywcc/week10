ttt_board = [['X', 'O', 'X'],['O', 'X', 'X'],['X', 'O', 'O']]

matrix = ((1,3,5),(5,7,9),(2,3,4))


print(matrix)

the_sum = 0

for row in matrix:
    for item in row:
        the_sum += item

print(the_sum)
