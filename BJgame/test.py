from classes import Card, Deck, Hand ,Chips
from funcs import show_some, hit_or_stand, hit, take_bet
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
deck = Deck()

''' deal card to dealer and two cards for human'''
dealer = Hand()
player = Hand()
p_chips=Chips('player',100)
d_chips=Chips('delaer',100)
take_bet(p_chips)
'''
hit_or_stand(deck,player)

show_some(player,dealer)
'''
