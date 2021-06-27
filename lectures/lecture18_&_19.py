import random

# data types
    # bool
    # string
    # turtle
    # etc.

# HOW TO CREATE YOUR OWN DATA TYPE:

class Point:
    def __init__(self, xcoord=0,ycoord=0):
        '''(Point, float, float) -> None'''
        self.x = xcoord
        self.y = ycoord

    def reflect_y(self):
        self.x = - self.x

    def reflect_x(self):
        self.y = - self.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __eq__(ob1, ob2):
        return ob1.x == ob2.x and ob1.y == ob2.y

    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        return 'I am a point with coordinates: (' +str(self.x)+','+str(self.y)+')'
        

# When you make a call Point(2,3), what happens?
#
# 1. object of type Point gets created
# 2. The address of that object gets assigned to variable self
# 3. __init__ function gets executed


class Circle:

    pi = 3.14

    def __init__(self, xcoord, ycoord, radius):
        self.x = xcoord
        self.y = ycoord
        self.radius = radius

    def area(self):
        return self.radius**2 * Circle.pi


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def setRank(self, rank):
        self.rank = rank

    def __repr__(self):
        return 'Card('+self.rank+','+self.suit+')'

    def __str__(self):
        return self.rank+self.suit
    

class Deck:

    suits={'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks={'A','2','3','4','5','6','7','8','9','10','J','Q','K'}

    def __init__(self):
        self.deck=[]
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.deck)

    
