state_name = 'Mississippi'

s_count = 0

for char in state_name:
    if char.capitalize() == 'S':
        s_count += 1

print('there are', s_count, 'of s\'s in', state_name)