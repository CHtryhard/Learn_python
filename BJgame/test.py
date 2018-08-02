from classes import Card, Deck, Hand
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
deck = Deck()

''' deal card to dealer and two cards for human'''
dealer = Hand()
player = Hand()
card1=deck.deal()
print("Dealer's Cards:")
print(card1)
dealer.add(card1)
dealer.add(deck.deal())
card1=deck.deal()
print("Player's Cards:")
print(card1)
player.add(card1)
card2=deck.deal()
print(card2)
player.add(card2)
