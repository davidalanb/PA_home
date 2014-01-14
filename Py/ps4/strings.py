'''
Strings are immutable
'''

print( '------------ basics & iterating --------------' )

# make reference to string
s = "Benedetto"

# basics
print( s )
print( len( s ) )
print( s[0], s[-1] )

# one way to iterate
for letter in s:
    print( letter, end='.' )
print()

# 2nd way:  iterate with index
for i in range( len(s) ):
    print( s[i], end='-' )
print()

# getting slices
print( s[0:4] )
print( s[4:len(s)] )

print('#------------------- find ---------------')

# find() returns index, or -1 if sub not found
i = s.find( 'n' )
print(i, '\t', s[i] )

# works with substrings
sub = 'detto'
i = s.find( sub )
print( i, '\t', s[i:(i+len(sub))] )

# start at the beginning
i = s.find( 'e' )
print(i, '\t', s[i] )

# start looking after the previous find
i = s.find( 'e', i+1 )
print(i, '\t', s[i] )

# and again...
i = s.find( 'e', i+1 )
print(i, '\t', s[i] )

# one more time... returns -1 because we're out of e's!
i = s.find( 'e', i+1 )
print(i)

print('#--------------- manipulate ----------------------')

s = "Benedetto"

# returns s with all letters to uppercase,
#   doesn't change s!!!
print( s.upper() )

s = "Benedetto"

# all letters to lowercast
print( s.lower() )

# replace characters
print( s.replace( 'e', 'o' ) )

# remember: s hasn't changed
print( s )

print('#--------------- split --------------------------')

# define & print string with spaces
ss = "This is a test"
print( ss )

# split by spaces
ls = ss.split()
print( ls )

# rejoin with commas
ss = ','.join(ls)
print( ss )

# split by commas
ls = ss.split(',')
print( ls )



