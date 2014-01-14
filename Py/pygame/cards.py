import random

class Card():

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def __str__(self):

        rank_map = {1:'A',11:'J',12:'Q',13:'K'}

        r = self.rank
        if r in rank_map:
            r = rank_map[r]

        suit_map = {0:'C',1:'S',2:'H',3:'D'}

        s = self.suit
        if s in suit_map:
            s = suit_map[s]

        return str(r) + str(s)

class Deck():

    def __init__(self):

        self.cards = []

        for i in range(52):

            suit = i // 13
            rank = i%13 + 1

            self.cards.append( Card( suit, rank) )

    def print(self, end='\n'):
        for i in range(52):
            self.cards[i].print(end)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal( self, nhands, ncards ):

        self.shuffle()
        hands = []

        for i in range(nhands):
            hands.append(Hand())
            for j in range(ncards):
                print( i*ncards+j )
                card = self.cards[i*ncards+j]
                hands[i].draw([card])

        return hands

class Hand():

    def __init__(self):
        self.cards = []

    def draw( self, cards ):
        for c in cards:
            self.cards.append(c)

    def play(self,n=1):
        if n==1:
            return [self.cards.pop(0)]
        else:
            cards = []
            for i in range(n):
                cards.append(self.cards.pop(0))
            return cards

    def pairs(self):
        pairs=[]
        for c1 in self.cards:
            for c2 in self.cards:
                if c1 is c2:
                    pass
                else:
                    if c1.rank == c2.rank:
                        if not (c2,c1) in pairs:
                            pairs.append( (c1,c2) )
        return pairs

class Game():

    def __init__( self ):
        self.deck = Deck()

    def deal( self, nhands, ncards ):

        self.deck.shuffle()
        hands = []

        for i in range(nhands):
            hands.append(Hand())
            for j in range(ncards):
                print( i*ncards+j )
                card = self.deck.cards[i*ncards+j]
                hands[i].draw([card])

        return hands


class War(Game):

    def __init__(self):
        super().__init__()
        self.hands=[]

    def play_trick(self):

       # each player plays a card
        p1,p2 = self.hands[0].play()[0], self.hands[1].play()[0]

        print( 'p1:',p1,'\tp2:',p2 )

        if p1.rank == p2.rank:
            print( "War!!!" )

            #TODO:  what happens if a player has no cards left?

            if len(self.hands[0].cards) < 4:
                k1 = self.hands[0].play( len(self.hands[0].cards)-1 )
            else:
                k1 = self.hands[0].play(3)

            if len(self.hands[1].cards) < 4:
                k2 = self.hands[1].play( len(self.hands[1].cards)-1 )
            else:
                k2 = self.hands[1].play(3)

            # now compare cards again - need recursion
            winner = self.play_trick()

            print( '\t', ', '.join(str(card) for card in k1) )
            print( '\t', ', '.join(str(card) for card in k2) )

            self.hands[winner].draw(k1+k2)
            self.hands[winner].draw( (p1,p2) )

            return winner
        elif p1.rank > p2.rank or p1.rank==1:
            print('... p1 wins')
            self.hands[0].draw( (p1,p2) )
            return 0
        else:
            print('... p2 wins')
            self.hands[1].draw( (p1,p2) )
            return 1

    def automate(self):

        self.hands = self.deal( 2, 26 )

        trx = 1
        while( input() == '' ):

            print( '---trick',trx );trx +=1

            self.play_trick()

            print( 'p1:',len(self.hands[0].cards), '\tp2:',
                len(self.hands[1].cards) )

            if len(self.hands[0].cards)==0:
                print( 'Game over - p2 wins!' )
                break
            elif len(self.hands[1].cards)==0:
                print( 'Game over - p1 wins!' )
                break

if __name__=='__main__':
    game = War()
    game.automate()
