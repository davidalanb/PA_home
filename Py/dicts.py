

# make an empty dict
# use curly braces to distinguish from standard list
words = {}

# add an item to words
words[ 'python' ] = "A scary snake"

# print the whole thing
print( words )

# print one item by key
print( words[ 'python' ] )

# define another dict
words2 = { 'dictionary': 'a heavy book', \
            'class': 'a group of students' }

# add all keys/items in words2 to words
words.update( words2 )

# add another key/item
words.update( { 'object': 'something'} )

#change a definition
words.update( { 'class': 'an echelon of society'} )

print( words )

# iterate with keys, 2 ways:
#for key in words.keys():
for key in words:
    print( key, end='; ' )
print()

# iterate with values
for value in words.values():
    print( value, end='; ' )
print()

# iterate with keys and values
for key, value in words.items():
    print( key, ':', value, end='; ' )
print()

try:
    print( words[ 'key' ] )
except Exception as e:
    print( type(e) )

key = 'nasef'

# ask for permission
if key in words:
    print( words[ key ] )
else:
    print( 'key', key, 'not found' )

# ask for forgiveness
try:
    print( words[ key ] )
except KeyError:
    print( 'key',key,'not found' )


