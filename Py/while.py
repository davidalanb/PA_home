
# prints 0 to 9
for x in range(10):
    print( x )


# prints 0 to 9
x = 0
while( x < 10 ):
    print( x )
    x += 1

'''
x = input()
while ( x != "bye" ):
    print(x)
    x = input()
'''


while( 1 ):
    x = input()
    if x=='bye':
        break
    elif x=='shh':
        continue
    print(x)




