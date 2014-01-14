

def get_occurrences( s ):

    letters = {}

    for l in s.lower():
        if l.isalpha():

            if l in letters.keys():
                letters[l] += 1
            else:
                letters[l] = 1

    return letters

def print_table( d ):
    for key,value in sorted(d.items()):
        print( key, '\t', value )

#print_table(get_occurrences("the quick brown fox jumped over the lazy dog"))


def test( b ):
    assert( b )

def add_fruit(inventory, fruit, quantity=0):

    if fruit in inventory:
        inventory[fruit]+=quantity
    else:
        inventory[fruit]=quantity

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)