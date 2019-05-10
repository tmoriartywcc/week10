def calc_average(the_list):
    the_sum = 0

    for the_grade in the_list:
        the_sum += the_grade

    return the_sum / len(the_list)

def main():
    test_grades = [100,70,86,95]

    my_average = calc_average(test_grades)

    print('there are', len(test_grades), 'items in the list')
    print('the average is', my_average)




main()