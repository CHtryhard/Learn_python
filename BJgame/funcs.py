def hit (deck,hand):
    card = deck.deal()
    hand.add(card)
    hand.adjust()

def show_some(player, dealer):
    print('\nplayer has points:{} with following cards'.format(player.points))
    for card in player.cards:
        print(card)
    print('\ndealer:')
    print('Hidden Card')
    for card in dealer.cards[1:]:
        print(card)
    print('\n')

def show_all(player, dealer):
    print('\nplayer:')
    for card in player.cards:
        print(card)
    print('\ndealer:')
    for card in dealer.cards:
        print(card)
    print('\n')

def take_bet(player):
    while True:
        try:
            bet = int(input("What's your bet?  :"))
            if bet > player.balance:
                print('You dont have enough chips')
            else:
                print('bet has been placed')
                break
        except:
            print('please enter a integer')
    return bet

def player_busts():
    global playing
    playing = False
    p_bust = True
    return p_bust

def hit_or_stand (deck, hand):
    while True:
        judgment = input('Do you want to hit or stand? (type in h / s)')
        if judgment == 'h':
            hit(deck, hand)
            playing = True
            return playing
            break
        elif judgment == 's':
            playing = False
            return playing
            break
        else:
            print('Please enter a h or s.')
