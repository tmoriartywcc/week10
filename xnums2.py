student_xnums = ['X00001111', 'X00001112', 'X00001113', 'X00001114']

my_xnum = input('please enter xnum to look for:')

try:
    the_result = student_xnums.index(my_xnum)
    print('found', my_xnum, 'at position', the_result)
except ValueError:
    print(my_xnum, 'not found')