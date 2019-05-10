
def xnum_validate(the_xnum):
    start_ok = False
    len_ok = False
    digits_ok = False
    if the_xnum.startswith('X'):
        start_ok = True
    if len(the_xnum)== 9:
        len_ok = True

    number_part = the_xnum[1:]

    if number_part.isdigit():
        digits_ok = True

    return start_ok and len_ok and digits_ok

def main():
    the_num = input('enter xnum: ')

    if xnum_validate(the_num):
        print('the xnum validated')
    else:
        print('invalid xnum')

main()