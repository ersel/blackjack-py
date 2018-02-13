from random import shuffle
from libs.card import Card, CARD_VALUES

class Deck:

    def __init__(self, set_of_decks):
        self.cards = []

        if set_of_decks < 1:
            raise ValueError('Set of decks must be at least 1')

        self.set_of_decks = set_of_decks
        self.create()

    def create(self):
        # a single deck is 52 cards
        # 13 distinct cards
        # so 4 * 13
        SINGLE_DECK = 4

        cards = CARD_VALUES.keys()
        for i in range(SINGLE_DECK * self.set_of_decks):
            for card in cards:
                new_card = Card(card)
                self.cards.append(new_card)

    def shuffle(self):
        shuffle(self.cards)

    def pick(self):
        if self.cards:
            return self.cards.pop()

        return None

    def reset(self):
        self.cards = []
        self.create()
