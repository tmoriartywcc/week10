state_name = 'Mississippi'

print('string length is', len(state_name))

print('string is', state_name)
index_num = int(input('enter character position to capitalize(max number is ' + str(len(state_name))  + '):'))

try:
    print(state_name[index_num-1].capitalize())
except IndexError:
    print('invaild position number')