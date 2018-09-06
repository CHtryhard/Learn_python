#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the pcuter. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.deck = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffling Deck")
        random.shuffle(self.deck)

    def splitting(self):
        return (self.deck[:26],self.deck[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()





class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0




######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck = Deck()
deck.shuffle()
A,B = deck.splitting()
player = Player('Player',Hand(A))
pc = Player('Pc',Hand(B))

total_rounds = 0
war_count = 0

while player.still_has_cards() and pc.still_has_cards():
    total_rounds +=1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(player.name+" count: "+str(len(player.hand.cards)))
    print(pc.name+" count: "+str(len(pc.hand.cards)))
    print("Both players play a card!")
    print('\n')


    table_cards = []


    c_card = pc.play_card()
    p_card = player.play_card()

    table_cards.append(p_card)
    table_cards.append(c_card)
    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(player.remove_war_cards())
        table_cards.extend(pc.remove_war_cards())

        # Play cards
        c_card = pc.play_card()
        p_card = player.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(player.name+" has the higher card, adding to hand.")
            player.hand.add(table_cards)
        else:
            print(pc.name+" has the higher card, adding to hand.")
            pc.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(player.name+" has the higher card, adding to hand.")
            player.hand.add(table_cards)
        else:
            print(pc.name+" has the higher card, adding to hand.")
            pc.hand.add(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
