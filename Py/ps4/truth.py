'''
Truth tables
'''

# Print TT for and
print( "a\t\t b\t\t a and b")
for a in (False, True):
    for b in (False, True):
        print( a, '\t', b, '\t', (a and b))

# print TT for or
print( "\na\t\t b\t\t a or b")
for a in (False, True):
    for b in (False, True):
        print( a, '\t', b, '\t', (a or b))

# print TT for not
print( "\na\t\t not a")
for a in (False, True):
    print( a, '\t', (not a))