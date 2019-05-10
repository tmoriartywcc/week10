the_numbers = [100,70,30,10,50,200,1000]

the_numbers_copy = [] + the_numbers

#for item in the_numbers:
 #   the_numbers_copy.append(item)

print('original:', the_numbers)
print('copy:', the_numbers_copy)

the_numbers_copy[0] = 10000

print('original:', the_numbers)
print('copy:', the_numbers_copy)