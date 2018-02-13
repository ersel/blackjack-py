import getpass
from libs.card import Card
from libs.deck import Deck
from libs.hand import Hand
from libs.player import Player

house = Player(0)
user = getpass.getuser()

print('Welcome to Terminal Casino')
deposit = input('How much would you like to play with today {}? £'.format(user))
player = Player(int(deposit))
print('Joining a Blackjack table')

deck = Deck(8)
deck.shuffle()

while(player.balance > 0):
    # start a new round
    # get 2 cards for house
    house_hand = Hand()
    h1 = deck.pick()
    h2 = deck.pick()
    house_hand.dealt_card(h1)
    house_hand.dealt_card(h2)

    # serve 2 cards for user
    player.hands = []
    c1 = deck.pick()
    c2 = deck.pick()
    hand = Hand()
    hand.dealt_card(c1)
    hand.dealt_card(c2)
    player.hands.append(hand)

    # round continues until player plays all their hands
    while(not player.hands_played()):
        print('\nHouse holds {} X'.format(h1.card))
        print('\nYou hold:')
        for index, hand in enumerate(player.hands):
            hand_no = index + 1
            print('Hand {}: {}'.format(hand_no, hand))

        hand_to_play = player.get_hand_to_play()
        while(not hand_to_play.is_finalized()):
            print('\nNow playing hand: {}'.format(hand_to_play))
            print('What would you like to do?')
            options = hand_to_play.get_options(h1)
            for index, option in enumerate(options):
                print('{}: {}'.format(index + 1, option))
            selected = int(input('Enter the option number: '))
            action = options[selected - 1]
            if (action == 'HIT'):
                new_card = deck.pick()
                print('Dealt new card {}'.format(new_card.card))
                hand_to_play.dealt_card(new_card)
            elif (action == 'STAND'):
                hand_to_play.stand()
            elif (action == 'DOUBLE'):
                new_card = deck.pick()
                print('Hit me! {}'.format(new_card.card))
                hand_to_play.dealt_card(new_card)
                hand_to_play.stand()
            elif (action == 'SPLIT'):
                cards_to_split = hand_to_play.split()
                player.hands = []
                # get 2 new cards and hands
                new_card1 = deck.pick()
                new_card2 = deck.pick()
                new_hand1 = Hand()
                new_hand2 = Hand()
                new_hand1.cards = [cards_to_split[0], new_card1]
                new_hand2.cards = [cards_to_split[1], new_card2]
                player.hands.extend([new_hand1, new_hand2])
                hand_to_play = new_hand1
                print('\nSplitted! You now hold:')
                for index, hand in enumerate(player.hands):
                    hand_no = index + 1
                    print('Hand {}: {}'.format(hand_no, hand))
        # write an option parser function
        # apply option [hit, stand, split, double]
        # update hand definition to set hand as finalized
        # after drawing a card causes blackjack or total bust

    # apply house strategy
    # compare the results of house and players hands
    # filter out everything above 21, get highest of softs and hards
    # print who won
    # reset and shuffle deck
    # reset player stake and insurance



