import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank +' of '+ self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    def __str__(self):
        deck_show = ''
        for card in self.deck:
            deck_show += '\n' + card.__str__()
        return 'The deck has:' + deck_show
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()

class Hand:
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 0
    def add(self, card):
        card = card.split()
        self.cards.append(card)
        self.points += values.get(card[0])
        if card[2] == 'Ace':
            self.aces +=1
    def adjust(self):
        num = input('How many aces out of {} you want to be 1?'.format(self.aces))
        self.points -=num*10
