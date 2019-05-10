student_xnums = ['X00001111', 'X00001112', 'X00001113', 'X00001114']

print('length of the list is', len(student_xnums))

print(student_xnums)
try:
    del student_xnums[0]
except IndexError:
    print('invalid index')

print(student_xnums)