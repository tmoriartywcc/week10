student_xnums = ['X00001111', 'X00001112', 'X00001113', 'X00001114']
student_xnums.reverse()
print(student_xnums)

my_xnum = input('please enter xnum to drop:')

print('before:', student_xnums)
try:
    student_xnums.remove(my_xnum)
except ValueError:
    print('could not remove', my_xnum)
print('after:', student_xnums)


