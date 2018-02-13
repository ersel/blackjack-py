from libs.card import Card

class Hand:

    def __init__(self, is_split=False):
        self.cards = []
        self.standing = False
        self.splited = is_split

    def dealt_card(self, card):
        if not isinstance(card, Card):
            raise ValueError('Expecting a Card object, got {} instead'.format(type(card)))

        self.cards.append(card)

    def calculate_hard(self):
        return sum([card.get_value()[0] for card in self.cards])

    def calculate_soft(self):
        # see if there are any Aces in the hand
        # count one of them as 11, rest as 1
        aces = [card for card in self.cards if card.get_name() == 'Ace']
        rest = [card for card in self.cards if card.get_name() != 'Ace']
        aces_total = 0
        if aces:
            aces_total = aces[0].get_value()[1] + sum([ace.get_value()[0] for ace in aces[1:]])

        rest_total = sum([card.get_value()[0] for card in rest])
        return aces_total + rest_total

    def is_finalized(self):
        # hand is finalized
        # if player has a blackjack
        # or both soft and hard hands are over 21
        # or player has decided to stand
        soft = self.calculate_soft()
        hard = self.calculate_hard()

        if 21 in [soft, hard]:
            return True

        if soft > 21 and hard > 21:
            return True

        if self.standing:
            return True

        return False

    def get_options(self, dealer_open_card):
        if self.is_finalized():
            return []

        options = ['HIT', 'STAND']
        initial_round = True if len(self.cards) == 2 else False

        if (initial_round):
            options.append('SURRENDER')

            if (not self.splited and dealer_open_card.get_name() == 'Ace'):
                options.append('INSURANCE')

            if (not self.splited and self.cards[0].get_name() == self.cards[1].get_name()):
                options.append('SPLIT')

        soft = self.calculate_soft()
        hard = self.calculate_hard()
        double_range = [9, 10, 11]
        if (soft in double_range or hard in double_range):
            options.append('DOUBLE')

        return options

    def stand(self):
        self.standing = True

    def split(self):
        initial_round = True if len(self.cards) == 2 else False
        if (initial_round and self.cards[0].get_name() == self.cards[1].get_name()):
            return self.cards

        return []

    def get_score(self):
        soft = self.calculate_soft()
        hard = self.calculate_hard()
        try:
            return max([s for s in [soft, hard] if s < 22])
        except:
            return 0

    def __str__(self):
        out = ''
        soft = self.calculate_soft()
        hard = self.calculate_hard()
        for card in self.cards:
            out += '{} '.format(card.card)
        return '{} | Soft: {} | Hard: {} |'.format(out, soft, hard)
