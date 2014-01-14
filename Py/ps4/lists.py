'''
Lists are mutable
'''

print( '----------- identical to string methods ---------------' )

# type-casting:  make a list out of a string
s = "Benedetto"
ls = list(s)

# basics
print( ls )
print( len( ls ) )
print( ls[0], ls[-1] )

# one way to iterate
for letter in ls:
    print( letter, end='.' )
print()

# 2nd way:  iterate with index
for i in range( len(ls) ):
    print( ls[i], end='-' )
print()

# getting slices
print( ls[0:4] )
print( ls[4:len(s)] )

print( '----------- add / remove ---------------' )

# setup
ls = [ "joe", "jane" ]
print( ls )

# a couple ways to append
ls.append( "rob" )
ls += [ "bill", "phoebe" ]
print( ls )

# insert at a given index
ls.insert( 2, "marcus" )
print( ls )

# pop removes and returns one element by index
name = ls.pop(2)
print( name, ls )

# del removes one of more elements by index[es]
outcasts = ls[2:4]
del( ls[2:4] )
print( outcasts, ls )

# remove a found element
ls.remove( 'phoebe' )
print( ls )

print( '--- alias & clone ---' )

ls1 = ['joe','bob']
ls2 = ls1               # make another reference to same list
ls2.remove( 'bob' )     # ls1 and ls2 refer to only one list
print( 'ls1: ', ls1 )

ls1 = ['joe','bob']
ls2 = ls1[:]            # make a clone of ls1 called ls2
ls2.remove('bob')       # modify ls2
print( 'ls1: ', ls1 )   # see that ls1 hasn't changed
print( 'ls2: ', ls2 )

print( '----------- sort --------------' )

ls = list("ngieaNDGNIEWSK, .,42764(*&^(*^@")
ls.sort()
for item in ls: print( item, end=' ')







