student_xnums = ('X00001111', 'X00001112', 'X00001113', 'X00001114')

my_xnum = input('please enter xnum to look for:')

if my_xnum in student_xnums:
    print('its in there')
else:
    print('its not')

print(student_xnums)
my_xnum = input('enter xnum to add:')
student_xnums.append(my_xnum)
print(student_xnums)
