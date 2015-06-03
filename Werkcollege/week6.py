import random
from itertools import groupby, count

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self,x=None,y=None):
        if x is None:
            self.x=0.0
            self.y=0.0
        else:
            self.x=x
            self.y=y
    
    def __str__(self):
        return '(%s,%s)' % (self.x,self.y)
    
    def __add__(self,other):
        if isinstance(other, Point):
            return self.add_points(other)
        else:
            return self.add_tuple(other)
    
    def add_points(self,other):
        newpointx=self.x+other.x
        newpointy=self.y+other.y
        return Point(newpointx,newpointy)
    
    def add_tuple(self,other):
        tupx=self.x+other[0]
        tupy=self.y+other[1]
        return Point(tupx,tupy)

class Kangaroo(object):
    def __init__(self):
        self.pouch_contents=[]
    
    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

#testp1=Point(1,1)
#testp2=Point(0,4)
#testtuple=(3,3)
#print(testp1+testtuple)
#print(testp1+testp2)

#kanga = Kangaroo()
#roo = Kangaroo()
#kanga.put_in_pouch('wallet')
#kanga.put_in_pouch('car keys')
#kanga.put_in_pouch(roo)
#print(kanga)
#print(roo)

class Card(object):
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    
    suit_names=['Clubs','Diamonds','Hearts','Spades']
    rank_names=[None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
    
    def __lt__(self,other):
        if self.suit>other.suit:
            return False
        if self.suit<other.suit:
            return True
        
        if self.rank>other.rank:
            return False
        if self.rank<other.rank:
            return True

    def __gt__(self,other):
        if self.suit>other.suit:
            return True
        if self.suit<other.suit:
            return False
        
        if self.rank>other.rank:
            return True
        if self.rank<other.rank:
            return False
    
    def __eq__(self,other):
        if self.suit==other.suit and self.rank==other.rank:
            return True
        return False

#card1=Card(2,11)
#card2=Card(1,12)
#print(card1==card2)

class Deck(object):
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self,card):
        return self.cards.append(card)
    
    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
    
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
    def deal_hands(self,hands,numb):
        lijst=[]
        for k in range(hands):
            hand=Hand('Hand number is '+str(k))
            self.move_cards(hand,numb)
            lijst.append(hand)
        return lijst

class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label=label

class PokerHand(Hand):
    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair']

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        self.suit_hist()
        suits=self.suits
        for val in suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        ranks=self.ranks
        for val in ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_twopair(self):
        self.rank_hist()
        ranks=self.ranks
        pairs=0
        for val in ranks.values():
            if val >= 2:
                pairs+=1
        if pairs>=2:
            return True
        return False
    
    def has_threekind(self):
        self.rank_hist()
        ranks=self.ranks
        for val in ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        self.rank_hist()
        self.keylijst=[]
        for key in self.ranks.keys():
            self.keylijst.append(key)
        self.keylijst.sort()
        for _, g in groupby(self.keylijst, lambda n, c=count(): n-next(c)):
            l=list(g)
            if len(l)>=5:
                return True
        return False

    def has_fourkind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
    
    def has_fullhouse(self):
        if self.has_twopair()==True:
            if self.has_threekind()==True:
                return True
        return False
    
    def has_straightflush(self):
        if self.has_straight()==True:
            if self.has_flush()==True:
                return True
        return False

    def classify(self):
        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)

histogram=[0,0,0,0,0,0,0,0]
n=10000

for k in range(n):
    deck = Deck()
    deck.shuffle()

    for i in range(5):
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        hand.classify()
        for i in range(8):
            if hand.labels==[]:
                break
            if PokerHand.all_labels[i]==hand.labels[0]:
                histogram[i]+=1

print(histogram)
newhist = [x / (n*5) for x in histogram]
print(newhist)