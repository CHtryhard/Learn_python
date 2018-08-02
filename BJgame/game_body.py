from classes import Card, Deck, Hand ,Chips
from funcs import show_some, hit, take_bet, player_busts, show_all, hit_or_stand

game = True
p_b = False
# Set up the Player's chips
p_chips=Chips('player',100)
d_chips=Chips('delaer',1000)
while game:
    # Print an opening statement
    print('Welcome to the Black jack game!')
    if p_chips.balance <= 0:
        print ('you have no chips to play')
        break
    else:
        pass
    # Create & shuffle the deck, deal two cards to each player
    playing = True
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    player.add(deck.deal())
    player.add(deck.deal())
    dealer.add(deck.deal())
    dealer.add(deck.deal())

    # Prompt the Player for their bet
    bet = take_bet(p_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        playing = hit_or_stand(deck,player)
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.points > 21:
            p_b = player_busts()
            break
        else:
            continue

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if p_b == True:
        print('Player bust')
        p_chips.lose(bet)
        d_chips.win(bet)
        show_all(player, dealer)
    else:
        while dealer.points <= 17:
            hit(deck, dealer)
            show_some(player,dealer)
        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if dealer.points > 21:
            print('Dealer bust')
            show_all(player, dealer)
            p_chips.win(bet)
            d_chips.lose(bet)
        elif player.points > dealer.points:
            print('Player win')
            show_all(player, dealer)
            p_chips.win(bet)
            d_chips.lose(bet)
        else:
            print('Dealer win')
            show_all(player, dealer)
            p_chips.lose(bet)
            d_chips.win(bet)
    # Inform Player of their chips total
    print(p_chips)
    print(d_chips)
    # Ask to play again
    while True:
        answer = input('do you want to play agian ? y/n')
        if answer == 'y':
            game = True
            break
        elif answer == 'n':
            game = False
            print('thanks for playing')
            break
        else:
            print('please input valid answer')
