test_names = ['Quiz1', 'Quiz2', 'Midterm', 'Final']
test_grades = [100,70,86,95]

print('first item in list is', test_grades[0])

print('the list is', test_grades)

the_sum = 0

for the_grade in test_grades:
    the_sum += the_grade

print('there are', len(test_grades), 'items in the list')
print(the_sum / len(test_grades))

try:
    test_grades[10] = 100
    test_grades[-1] = 100
except IndexError:
    print('error with index number')

print('the list is', test_grades)

the_sum = 0

for the_grade in test_grades:
    the_sum += the_grade

print('there are', len(test_grades), 'items in the list')
print(the_sum / len(test_grades))
