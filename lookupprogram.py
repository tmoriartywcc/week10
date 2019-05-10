import wccemail

my_lookup = wccemail.create_lookup_table()

try:
    the_xnum = wccemail.lookup_xnum(my_lookup, 'X00001112')
    print(the_xnum)
except KeyError:
    print('key not found')