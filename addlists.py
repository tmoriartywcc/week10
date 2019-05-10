list1 = [1,2,3,4]
list1 += [5,6,7,8]

new_list = list1[4:]

print(new_list)

num_item = 0
for num in new_list:
    if num_item != len(new_list) - 1:
        print(num, ",", sep='', end='')
    else:
        print(num, sep='', end='')
    num_item+=1