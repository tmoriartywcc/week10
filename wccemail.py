def create_lookup_table():
    email_lookup = {'X00001111':'foo1@waubonsee.edu',
                    'X00002222':'student1@waubonsee.edu',
                    'X00110011':'admin@waubonsee.edu'}
    return email_lookup

def lookup_xnum(lookup_table, xnum):
    return lookup_table[xnum]

def update_email(lookup_table, xnum, new_email):
    lookup_table[xnum] = new_email

def add_email(lookup_table, xnum, new_email):
    lookup_table[xnum] = new_email

def remove_email(lookup_table, xnum):
    del lookup_table['X22222222']
