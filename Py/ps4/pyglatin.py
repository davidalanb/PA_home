'''
pygLatin.py
'''

def pygLatin( s ):

    # tokenize
    tokens = s.split(' ')

    for i,t in enumerate(tokens):

        t = t.lower()

        # if word begins with a vowel
        if t[0] in ['a','e','i','o','u']:
            tokens[i] = t + "-way"

        else:
            for j,l in enumerate(t):
                if l in ['a','e','i','o','u']:
                    tokens[i] = t[j:len(t)] + '-' + t[0:j] + 'ay'
                    break


    return ' '.join(tokens)


def main():

    print(pygLatin("I'm going to the store"))

if __name__ == '__main__':
    main()
